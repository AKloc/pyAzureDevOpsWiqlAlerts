#!python3
import json
from utilities.azure_devops_interface import azure_devops_interface

def lambda_handler(event, context):
    f = azure_devops_interface()
    f.passthrough_method('Derp')
    
    return {
        'statusCode': 200,
        'body': json.dumps('azure_devops_interface did stuff.')
    }


