#!python3
import json
from utilities.azure_devops_interface import azure_devops_interface

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda - MODIFIED!')
    }


f = azure_devops_interface()
f.passthrough_method('Derp')