#! python3
import boto3
from .alert import Alert


# Note - need to have AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
# environment variables.
class AlertProcessor:
    def __init__(self):
        self._dynamodb_connection = boto3.resource('dynamodb', region_name='us-east-1')
        alerts_table = self._dynamodb_connection.Table('alerts')

        # Get everything in the table.
        alerts_table_items = alerts_table.scan()

        self._alert_configs = []

        for alert_config in alerts_table_items['Items']:
            alert_name = alert_config['alert_name']
            slack_webhook_uri = alert_config['slack_webhook_uri']
            azure_devops_query_config = alert_config['azure_devops_query']
            f_string_header = alert_config['f_string_header']
            f_string_footer = alert_config['f_string_footer']
            f_string_item = alert_config['f_string_item']
            print(f'Found an alert with alert_name {alert_name}.')

            alert_to_process = Alert(
                alert_name=alert_name,
                slack_webhook_uri=slack_webhook_uri,
                azure_devops_query_config=azure_devops_query_config,
                f_string_header=f_string_header,
                f_string_footer=f_string_footer,
                f_string_item=f_string_item)

            self._alert_configs.append(alert_to_process)

    def process_alerts(self) -> None:
        for alert in self._alert_configs:
            alert.process()
