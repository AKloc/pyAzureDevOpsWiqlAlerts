#! python3
import boto3


class AlertCreator:
    def __init__(self):
        self._dynamodb_connection = boto3.resource('dynamodb', region_name='us-east-1')
        self._alerts_table = self._dynamodb_connection.Table('alerts')

    def create_item(self, alert_name, slack_webhook_uri, azure_devops_query_config, f_string_header='',
                 f_string_footer='', f_string_item=''):
        response = self._alerts_table.put_item(
            Item={
                'alert_name': alert_name,
                'azure_devops_query': {
                    'api_token': azure_devops_query_config['api_token'],
                    'query_id': azure_devops_query_config['query_id'],
                    'query_uri': azure_devops_query_config['query_uri']
                },
                'f_string_footer': f_string_footer,
                'f_string_header': f_string_header,
                'f_string_item': f_string_item,
                'slack_webhook_uri': slack_webhook_uri
            }
        )

        return response
