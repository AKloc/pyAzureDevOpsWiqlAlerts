#! python3
import boto3
from .alert import Alert


# Note - need to have AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
# environment variables.
class AlertsGenerator:
    def __init__(self):
        self._dynamodb_connection = boto3.resource('dynamodb', region_name='us-east-1')
        alerts_table = self._dynamodb_connection.Table('alerts')

        # Get everything in the table.
        all_alerts = alerts_table.scan()

        for alert_config in all_alerts['Items']:
            alert_name = alert_config['alert_name']
            slack_webhook_uri = alert_config['slack_webhook_uri']
            print(f'Found an alert with alert_name {alert_name}.')

            alert_to_process = Alert(
                alert_name=alert_name,
                slack_webhook_uri=slack_webhook_uri)

            alert_to_process.azure_devops_query_config = alert_config['azure_devops_query']

            alert_to_process.process()