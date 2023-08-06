#!/usr/bin/env python3

import os
import time
import re
import sys
import json
import argparse

import backoff
import pendulum
import requests
import dateutil.parser
import singer
import singer.metrics as metrics
from singer import utils


REQUIRED_CONFIG_KEYS = ["start_date", "api_key"]
PER_PAGE = 100
BASE_URL = "https://app.close.io/api/v1/"

CONFIG = {}
STATE = {}

LOGGER = singer.get_logger()
SESSION = requests.session()


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

def load_schema(entity):
    return utils.load_json(get_abs_path("schemas/{}.json".format(entity)))

def transform_datetime(datetime):
    if datetime is None:
        return None

    return pendulum.parse(datetime).format(utils.DATETIME_FMT)


def transform_datetimes(item, datetime_fields):
    if not isinstance(datetime_fields, list):
        datetime_fields = [datetime_fields]

    for k in datetime_fields:
        if k in item:
            item[k] = transform_datetime(item[k])


def get_start(key):
    if key not in STATE:
        STATE[key] = CONFIG['start_date']

    return STATE[key]


def parse_source_from_url(url):
    match = re.match(r'^(\w+)\/', url)
    if match:
        return match.group(1)


def request(endpoint, params=None):
    url = BASE_URL + endpoint
    params = params or {}
    headers = {}
    if 'user_agent' in CONFIG:
        headers['User-Agent'] = CONFIG['user_agent']

    auth = (CONFIG['api_key'], "")
    req = requests.Request("GET", url, params=params, auth=auth, headers=headers).prepare()
    LOGGER.info("GET {}".format(req.url))

    with metrics.http_request_timer(parse_source_from_url(endpoint)) as timer:
        resp = SESSION.send(req)
        timer.tags[metrics.Tag.http_status_code] = resp.status_code
        json = resp.json()

    # if we're hitting the rate limit cap, sleep until the limit resets
    if resp.headers.get('X-Rate-Limit-Remaining') == "0":
        time.sleep(int(resp.headers['X-Rate-Limit-Reset']))

    # if we're already over the limit, we'll get a 429
    # sleep for the rate_reset seconds and then retry
    if resp.status_code == 429:
        time.sleep(json["rate_reset"])
        return request(endpoint, params)

    resp.raise_for_status()

    return json


def gen_request(endpoint, params=None):
    params = params or {}
    params['_limit'] = PER_PAGE
    params['_skip'] = 0

    with metrics.record_counter(parse_source_from_url(endpoint)) as counter:
        while True:
            body = request(endpoint, params)
            for row in body['data']:
                counter.increment()
                yield row

            if not body.get("has_more"):
                break

            params['_skip'] += PER_PAGE



def transform_activity(activity):
    transform_datetimes(activity, ["date_scheduled"])

    # activity["envelope"]["date"] has many different formats, some of which
    # aren't recognized by pendulum. For this reason, we treat this field as a
    # string. Examples:
    # - Fri, 01 Feb 2013 00:54:51 +0000 (UTC)
    # - Fri, 19 May 2017 10:57:03 +0200 (added by foo@bar.com)
    # - 4/21/17 9:21 AM (GMT-05:00)

    if "send_attempts" in activity:
        for item in activity["send_attempts"]:
            transform_datetimes(item, ["date"])


def sync_activities():
    schema = load_schema("activities")
    singer.write_schema("activities", schema, ["id"])

    start = pendulum.parse(get_start("activities"))
    now = pendulum.now()

    while start <= now:
        end = start.add(days=1)
        params = {"date_created__gte": start, "date_created__lt": end}

        for row in gen_request("activity/", params):
            transform_activity(row)

            singer.write_record("activities", row)
            utils.update_state(STATE, "activities", dateutil.parser.parse(row['date_created']))

        start = start.add(days=1)
        singer.write_state(STATE)

def to_json_type(typ):
    if typ in ["datetime", "date"]:
        return {"type": ["null", "string"], "format": "date-time"}

    if typ == "number":
        return {"type": ["null", "number", "boolean"]}

    # According to the closeio docs on choices:
    # "Choices: a dropdown of predefined choices. Admins can set up all the possible
    # choices this field can contain ahead of time."
    # closeio docs on user:
    # "User: a dropdown containing all the users who are active in your organization."
    if typ in ["text", "choices", "user"]:
        return {"type": ["null", "string", "boolean"]}

    # According to the closeio docs on hidden:
    # "Hidden: a field that's never displayed in the UI, but can be useful for API integrations.
    # Accepts any data type from JSON, including lists and objects."
    if typ == 'hidden':
        return {}

    raise ValueError('Unexpected custom field type: {}'.format(typ))


def get_custom_leads_schema():
    return {
        "type": "object",
        "properties": {row["name"]: to_json_type(row["type"])
                       for row in gen_request("custom_fields/lead/")},
    }


def transform_lead(lead, custom_schema):
    if "tasks" in lead:
        for item in lead["tasks"]:
            transform_datetimes(item, ["date", "due_date"])

    if "opportunities" in lead:
        for item in lead["opportunities"]:
            transform_datetimes(item, ["date_won"])

    if "custom" in lead:
        custom_datetimes = [k for k, v in custom_schema["properties"].items()
                            if v.get("format") == "date-time"]
        transform_datetimes(lead["custom"], custom_datetimes)


def sync_leads():
    schema = load_schema("leads")
    custom_schema = get_custom_leads_schema()
    schema["properties"]["custom"] = custom_schema
    singer.write_schema("leads", schema, ["id"])

    start = get_start("leads")
    formatted_start = dateutil.parser.parse(start).strftime("%Y-%m-%d %H:%M")
    params = {'query': 'date_updated>="{}" sort:date_updated'.format(formatted_start)}

    for i, row in enumerate(gen_request("lead/", params)):
        transform_lead(row, custom_schema)
        row['contacts'] = [request("contact/{}/".format(contact['id']))
                           for contact in row['contacts']]
        if row['date_updated'] >= start:
            singer.write_record("leads", row)
            utils.update_state(STATE, "leads", dateutil.parser.parse(row['date_updated']))

        if i % PER_PAGE == 0:
            singer.write_state(STATE)

    singer.write_state(STATE)


def do_sync():
    LOGGER.info("Starting sync")
    sync_activities()
    sync_leads()
    LOGGER.info("Completed sync")


# Copied from singer-python to extend for catalog
def parse_args(required_config_keys):
    '''Parse standard command-line args.

    Parses the command-line arguments mentioned in the SPEC and the
    BEST_PRACTICES documents:

    -c,--config     Config file
    -s,--state      State file
    -d,--discover   Run in discover mode
    -p,--properties Properties file

    Returns the parsed args object from argparse. For each argument that
    point to JSON files (config, state, properties), we will automatically
    load and parse the JSON file.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--config',
        help='Config file',
        required=True)

    parser.add_argument(
        '--catalog',
        help='catalog')

    parser.add_argument(
        '-s', '--state',
        help='State file')

    parser.add_argument(
        '-p', '--properties',
        help='Property selections')

    parser.add_argument(
        '-d', '--discover',
        action='store_true',
        help='Do schema discovery')

    args = parser.parse_args()
    if args.config:
        args.config = utils.load_json(args.config)
    if args.state:
        args.state = utils.load_json(args.state)
    else:
        args.state = {}
    if args.properties:
        args.properties = utils.load_json(args.properties)

    check_config(args.config, required_config_keys)

    return args


# Copied from singer-python to extend for catalog
def check_config(config, required_keys):
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        raise Exception("Config is missing required keys: {}".format(missing_keys))


def main_impl():
    args = parse_args(REQUIRED_CONFIG_KEYS)
    if args.discover:
        json.dump({"streams": [{"tap_stream_id": "automatic_closeio_replication",
                                "stream": "automatic_closeio_replication"}]},
                  sys.stdout, indent=2)
        sys.exit(0)
    CONFIG.update(args.config)
    STATE.update(args.state)
    do_sync()

def main():
    try:
        main_impl()
    except Exception as exc:
        LOGGER.critical(exc)
        raise exc

if __name__ == "__main__":
    main()
