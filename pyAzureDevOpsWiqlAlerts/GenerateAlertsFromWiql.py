#!python3
import json
from pyAzureDevOpsWiqlAlerts.utilities.alertsgenerator import AlertsGenerator

def lambda_handler(event, context):
    # Fetch AWS environment variables

    alerts_generator = AlertsGenerator()
    alerts_generator.process_alerts()


    return {
        'statusCode': 200,
        'body': json.dumps('azure_devops_interface did stuff.')
    }


lambda_handler(None, None)
