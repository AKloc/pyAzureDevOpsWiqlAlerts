#! python 3
import boto3
from boto3.dynamodb.conditions import Key


class AlertGetter:
    def __init__(self, owner):
        self._dynamodb_connection = boto3.resource('dynamodb', region_name='us-east-1')
        self._alerts_table = self._dynamodb_connection.Table('alerts')
        self._owner = owner

    def get_items(self):
        response = self._alerts_table.query(
            IndexName = 'owner-index',
            KeyConditionExpression=Key('owner').eq(self._owner)
        )
        return response['Items']

    def get_item(self, alert_name):
        response = self._alerts_table.query(
            IndexName = 'alert_name-index',
            KeyConditionExpression=Key('alert_name').eq(alert_name)
        )
        return response['Items']

derp = AlertGetter('Weyland Yutani')
items = derp.get_items()
print(f'Got: {len(items)} items.')