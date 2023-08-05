import os
import json
import datetime
import pytz
import singer

from singer import metadata
from singer import utils
from singer.metrics import Point

LOGGER = singer.get_logger()
KEY_PROPERTIES = ['id']

CUSTOM_TYPES = {
    'text': 'string',
    'textarea': 'string',
    'date': 'string',
    'regexp': 'string',
    'dropdown': 'string',
    'integer': 'integer',
    'decimal': 'number',
    'checkbox': 'boolean',
}

def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

def process_custom_field(field):
    """ Take a custom field description and return a schema for it. """
    zendesk_type = field.type
    json_type = CUSTOM_TYPES.get(zendesk_type)
    if json_type is None:
        raise Exception("Discovered unsupported type for custom field {} (key: {}): {}"
                        .format(field.title,
                                field.key,
                                zendesk_type))
    field_schema = {'type': [
        json_type,
        'null'
    ]}

    if zendesk_type == 'date':
        field_schema['format'] = 'datetime'
    if zendesk_type == 'dropdown':
        field_schema['enum'] = [o['value'] for o in field.custom_field_options]

    return field_schema

class Stream():
    name = None
    replication_method = None
    replication_key = None
    key_properties = KEY_PROPERTIES
    stream = None

    def __init__(self, client=None):
        self.client = client

    def get_bookmark(self, state):
        return utils.strptime_with_tz(singer.get_bookmark(state, self.name, self.replication_key))

    def update_bookmark(self, state, value):
        current_bookmark = self.get_bookmark(state)
        if value and utils.strptime_with_tz(value) > current_bookmark:
            singer.write_bookmark(state, self.name, self.replication_key, value)

    def load_schema(self):
        schema_file = "schemas/{}.json".format(self.name)
        with open(get_abs_path(schema_file)) as f:
            schema = json.load(f)
        return self._add_custom_fields(schema)

    def _add_custom_fields(self, schema): # pylint: disable=no-self-use
        return schema

    def load_metadata(self):
        schema = self.load_schema()
        mdata = metadata.new()

        mdata = metadata.write(mdata, (), 'table-key-properties', self.key_properties)
        mdata = metadata.write(mdata, (), 'forced-replication-method', self.replication_method)

        if self.replication_key:
            mdata = metadata.write(mdata, (), 'valid-replication-keys', [self.replication_key])

        for field_name in schema['properties'].keys():
            if field_name in self.key_properties or field_name == self.replication_key:
                mdata = metadata.write(mdata, ('properties', field_name), 'inclusion', 'automatic')
            else:
                mdata = metadata.write(mdata, ('properties', field_name), 'inclusion', 'available')

        return metadata.to_list(mdata)

    def is_selected(self):
        return self.stream is not None

class Organizations(Stream):
    name = "organizations"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def _add_custom_fields(self, schema):
        endpoint = self.client.organizations.endpoint
        # NB: Zenpy doesn't have a public endpoint for this at time of writing
        #     Calling into underlying query method to grab all fields
        field_gen = self.client.organizations._query_zendesk(endpoint.organization_fields, # pylint: disable=protected-access
                                                             'organization_field')
        schema['properties']['organization_fields']['properties'] = {}
        for field in field_gen:
            schema['properties']['organization_fields']['properties'][field.key] = process_custom_field(field)

        return schema

    def sync(self, state):
        bookmark = self.get_bookmark(state)
        organizations = self.client.organizations.incremental(start_time=bookmark)
        for organization in organizations:
            self.update_bookmark(state, organization.updated_at)
            yield (self.stream, organization)

class Users(Stream):
    name = "users"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def _add_custom_fields(self, schema):
        field_gen = self.client.user_fields()
        schema['properties']['user_fields']['properties'] = {}
        for field in field_gen:
            schema['properties']['user_fields']['properties'][field.key] = process_custom_field(field)

        return schema

    def sync(self, state):
        bookmark = self.get_bookmark(state)
        users = self.client.users.incremental(start_time=bookmark)
        for user in users:
            self.update_bookmark(state, user.updated_at)
            yield (self.stream, user)

class Tickets(Stream):
    name = "tickets"
    replication_method = "INCREMENTAL"
    replication_key = "generated_timestamp"

    last_record_emit = {}
    buf = {}
    buf_time = 60
    def _buffer_record(self, record):
        stream_name = record[0].tap_stream_id
        if self.last_record_emit.get(stream_name) is None:
            self.last_record_emit[stream_name] = utils.now()

        if self.buf.get(stream_name) is None:
            self.buf[stream_name] = []
        self.buf[stream_name].append(record)

        if (utils.now() - self.last_record_emit[stream_name]).total_seconds() > self.buf_time:
            self.last_record_emit[stream_name] = utils.now()
            return True

        return False

    def _empty_buffer(self):
        for stream_name, stream_buf in self.buf.items():
            for rec in stream_buf:
                yield rec
            self.buf[stream_name] = []

    def sync(self, state):
        bookmark = self.get_bookmark(state)
        tickets = self.client.tickets.incremental(start_time=bookmark)
        audits_stream = TicketAudits(self.client)
        metrics_stream = TicketMetrics(self.client)

        def emit_sub_stream_metrics(sub_stream):
            if sub_stream.is_selected():
                singer.metrics.log(LOGGER, Point(metric_type='counter',
                                                 metric=singer.metrics.Metric.record_count,
                                                 value=sub_stream.count,
                                                 tags={'endpoint':sub_stream.stream.tap_stream_id}))
                sub_stream.count = 0

        if audits_stream.is_selected():
            LOGGER.info("Syncing ticket_audits per ticket...")

        for ticket in tickets:
            generated_timestamp_dt = datetime.datetime.utcfromtimestamp(ticket.generated_timestamp).replace(tzinfo=pytz.UTC)
            self.update_bookmark(state, utils.strftime(generated_timestamp_dt))

            ticket_dict = ticket.to_dict()
            ticket_dict.pop('fields') # NB: Fields is a duplicate of custom_fields, remove before emitting
            is_deleted = (ticket_dict["status"] == "deleted")
            should_yield = self._buffer_record((self.stream, ticket_dict))

            if audits_stream.is_selected():
                if not is_deleted:
                    for audit in audits_stream.sync(ticket_dict["id"]):
                        self._buffer_record(audit)
                else:
                    LOGGER.warning("Unable to retrieve audits for deleted ticket (ID: %s), skipping...", ticket_dict["id"])

            if metrics_stream.is_selected():
                if not is_deleted:
                    for metric in metrics_stream.sync(ticket_dict["id"]):
                        self._buffer_record(metric)
                else:
                    LOGGER.warning("Unable to retrieve metrics for deleted ticket (ID: %s), skipping...", ticket_dict["id"])

            if should_yield:
                for rec in self._empty_buffer():
                    yield rec
                emit_sub_stream_metrics(audits_stream)
                emit_sub_stream_metrics(metrics_stream)
                singer.write_state(state)

        for rec in self._empty_buffer():
            yield rec
        emit_sub_stream_metrics(audits_stream)
        emit_sub_stream_metrics(metrics_stream)
        singer.write_state(state)

class TicketAudits(Stream):
    name = "ticket_audits"
    replication_method = "INCREMENTAL"
    count = 0

    def sync(self, ticket_id):
        ticket_audits = self.client.tickets.audits(ticket=ticket_id)
        for ticket_audit in ticket_audits:
            self.count += 1
            yield (self.stream, ticket_audit)

class TicketMetrics(Stream):
    name = "ticket_metrics"
    replication_method = "INCREMENTAL"
    count = 0

    def sync(self, ticket_id):
        ticket_metric = self.client.tickets.metrics(ticket=ticket_id)
        self.count += 1
        yield (self.stream, ticket_metric)

class Groups(Stream):
    name = "groups"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def sync(self, state):
        bookmark = self.get_bookmark(state)

        groups = self.client.groups()
        for group in groups:
            if utils.strptime_with_tz(group.updated_at) >= bookmark:
                self.update_bookmark(state, group.updated_at)
                yield (self.stream, group)

class Macros(Stream):
    name = "macros"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def sync(self, state):
        bookmark = self.get_bookmark(state)

        macros = self.client.macros()
        for macro in macros:
            if utils.strptime_with_tz(macro.updated_at) >= bookmark:
                self.update_bookmark(state, macro.updated_at)
                yield (self.stream, macro)

class Tags(Stream):
    name = "tags"
    replication_method = "FULL_TABLE"
    key_properties = ["name"]

    def sync(self, state): # pylint: disable=unused-argument
        # NB: Setting page to force it to paginate all tags, instead of just the
        #     top 100 popular tags
        tags = self.client.tags(page=1)
        for tag in tags:
            yield (self.stream, tag)

class TicketFields(Stream):
    name = "ticket_fields"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def sync(self, state):
        bookmark = self.get_bookmark(state)

        fields = self.client.ticket_fields()
        for field in fields:
            if utils.strptime_with_tz(field.updated_at) >= bookmark:
                self.update_bookmark(state, field.updated_at)
                yield (self.stream, field)

class GroupMemberships(Stream):
    name = "group_memberships"
    replication_method = "INCREMENTAL"
    replication_key = "updated_at"

    def sync(self, state):
        bookmark = self.get_bookmark(state)

        memberships = self.client.group_memberships()
        for membership in memberships:
            if utils.strptime_with_tz(membership.updated_at) >= bookmark:
                self.update_bookmark(state, membership.updated_at)
                yield (self.stream, membership)


STREAMS = {
    "tickets": Tickets,
    "groups": Groups,
    "users": Users,
    "organizations": Organizations,
    "ticket_audits": TicketAudits,
    "ticket_fields": TicketFields,
    "group_memberships": GroupMemberships,
    "macros": Macros,
    "tags": Tags,
    "ticket_metrics": TicketMetrics
}

    # stream = {
    #     "tap_stream_id": stream_name,
    #     "stream": stream_name,
    #     "key_properties": ["Id"],
    #     "schema": {
    #         "type": "object",
    #         "additionalProperties": False,
    #         "properties": properties,
    #     },
    #     'metadata': metadata.to_list(mdata)
    # }
