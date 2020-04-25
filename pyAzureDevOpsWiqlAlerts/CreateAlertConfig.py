#! python3
import json
from pyAzureDevOpsWiqlAlerts.utilities.AlertCreator import AlertCreator

def lambda_handler(event, context):

    alert_creator = AlertCreator()

    return {
        'statusCode': 201,
        'body': json.dumps('Alert successfully created.')
    }


lambda_handler(None, None)
