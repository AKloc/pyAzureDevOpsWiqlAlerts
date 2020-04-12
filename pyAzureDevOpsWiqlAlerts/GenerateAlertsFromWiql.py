#!python3
import json
from utilities.alertsgenerator import AlertsGenerator

def lambda_handler(event, context):
    # Fetch AWS environment variables

    alerts_generator = AlertsGenerator()


    return {
        'statusCode': 200,
        'body': json.dumps('azure_devops_interface did stuff.')
    }


lambda_handler(None, None)
