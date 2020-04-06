#! python3
import boto3
import json
import os

class alerts_generator:
    def __init__(self):
        # Fetch AWS environment variables
        if 'DYNAMODB_URI' in os.environ.keys():
            dynamodb_uri = os.environ['DYNAMODB_URI']
        else:
            dynamodb_uri = 'no uri set'

        if 'DYNAMODB_TABLE_NAME' in os.environ.keys():
            dynamodb_table_name = os.environ['DYNAMODB_TABLE_NAME']
        else:
            dynamodb_table_name = 'no uri set'

        self._dynamodb = boto3.resource('dynamodb', region_name='us-east', endpoint_url=dynamodb_uri)


        pass

