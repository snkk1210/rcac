import boto3
import os
import json
import datetime
import logging

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    CHANNEL_NAME = os.environ['channelName']
    HOOK_URL = os.environ['hookURL']

    fdocm = get_first_day_of_current_month()
    cost = get_cost_in_range(str(fdocm), str(datetime.date.today()))
    cost_amount = cost['ResultsByTime'][0]['Total']['NetUnblendedCost']['Amount']

    post_to_slack(HOOK_URL, CHANNEL_NAME, cost_amount, datetime.date.today())

    return 0

def get_first_day_of_current_month():
    """
    Returns the first date of the month.

    Parameters
    ----------
    none

    Returns
    -------
    first_day : string
    """
    today = datetime.date.today()
    first_day = today.replace(day=1)
    return first_day

def get_cost_in_range(start, end):
    """
    Returns the cost between specific dates.

    Parameters
    ----------
    start : string
        specific dates (A).
    end : string
        specific dates (B).

    Returns
    -------
    cost : dict
        API Return Values
    """
    ce = boto3.client('ce')
    cost = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End' :  end,
        },
        Granularity='MONTHLY',
        Metrics=[
            'NetUnblendedCost'
        ],
    )
    return cost

def post_to_slack(hook_url, channel_name, cost, day):
    """
    Post messages to Slack.

    Parameters
    ----------
    hook_url : string
        WEB Hook URL for Slack
    channel_name : string
        Channel Name for Slack
    cost : string
    day : string

    Returns
    -------
    0
    """
    slack_message = {
        "channel": channel_name,
        "icon_emoji": ":rotating_light:",
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "#FF0000",
                "title": "Billing: %s" % (day),
                "title_link": "https://us-east-1.console.aws.amazon.com/billing/home?region=us-east-1#/account",
                "text": "<!here>",
                "fields": [
                    {
                        "title": "Total",
                        "value": "USD %s" % (cost),
                        "short": True
                    }
                ]
            }
        ]
    }

    req = Request(hook_url, json.dumps(slack_message).encode('utf-8'))

    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)

    return 0
