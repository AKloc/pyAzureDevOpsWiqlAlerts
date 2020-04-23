#!python3
import json
from pyAzureDevOpsWiqlAlerts.utilities.AlertProcessor import AlertProcessor

def lambda_handler(event, context):

    alerts_generator = AlertProcessor()
    alerts_generator.process_alerts()

    return {
        'statusCode': 200,
        'body': json.dumps('Alerts generated and processed.')
    }

lambda_handler(None, None)