#! python3
import boto3
import json
import os

# Note - need to have AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY 
# environment variables.
class alerts_generator:
    def __init__(self):
        # Fetch AWS environment variables
        # if 'AWS_ACCESS_KEY_ID' in os.environ.keys():
        #     aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        # else:
        #     aws_access_key_id = 'no uri set'

        # if 'AWS_SECRET_ACCESS_KEY' in os.environ.keys():
        #     aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        # else:
        #     aws_secret_access_key = 'no uri set'

        self._dynamodb_connection = boto3.resource('dynamodb', region_name='us-east-1')
        alerts_table = self._dynamodb_connection.Table('alerts')

        # stuff = table.get_item(
        #     Key = {
        #         'alert_name': 'Refined Tickets Notification'
        #     }
        # )

        # Get everything in the table.
        all_alerts = alerts_table.scan()

        for alert in all_alerts['Items']:
            alert_name = alert['alert_name']
            print(f'Found an alert with alert_name {alert_name}.')
        
        # self._dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=dynamodb_uri)


        pass



#derp = alerts_generator()