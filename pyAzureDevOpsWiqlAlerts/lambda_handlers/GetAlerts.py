#!python3
import json
import sys
import urllib

sys.path.append("/opt/")  # needed to use AWS layers.
from utilities.AlertGetter import AlertGetter


def lambda_handler(event, context):
    alert_getter = AlertGetter('Weyland Yutani')
    path_parameters = event.get('pathParameters')

    if path_parameters is not None:
        alert_name = urllib.parse.unquote(path_parameters['name'])
        response = alert_getter.get_item(alert_name)
    else:
        response = alert_getter.get_items()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }