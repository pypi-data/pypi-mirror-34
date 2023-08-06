import json
from dateutil.parser import parse

import singer

from voluptuous import Schema, Required

LOGGER = singer.get_logger()

STATE_SCHEMA = Schema({
    Required('bookmarks'): {
        str: {
            Required('last_record'): str,
            Required('field'): str,
        }
    }
})


def get_last_record_value_for_table(state, table):
    to_return = state.get('bookmarks', {}) \
                .get(table, {}) \
                .get('last_record')

    if to_return is not None:
        to_return = parse(to_return)

    return to_return


def incorporate(state, table, field, value):
    if value is None:
        return state

    new_state = state.copy()

    parsed = parse(value).strftime("%Y-%m-%dT%H:%M:%SZ")

    if 'bookmarks' not in new_state:
        new_state['bookmarks'] = {}

    if(new_state['bookmarks'].get(table, {}).get('last_record') is None or
       new_state['bookmarks'].get(table, {}).get('last_record') < value):
        new_state['bookmarks'][table] = {
            'field': field,
            'last_record': parsed,
        }

    return new_state


def save_state(state):
    if not state:
        return

    STATE_SCHEMA(state)

    LOGGER.info('Updating state.')

    singer.write_state(state)


def load_state(filename):
    if filename is None:
        return {}

    try:
        with open(filename) as handle:
            return json.load(handle)
    except:
        LOGGER.fatal("Failed to decode state file. Is it valid json?")
        raise RuntimeError
