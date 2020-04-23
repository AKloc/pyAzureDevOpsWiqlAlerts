#! python3
import json

def lambda_handler(event, context):

    return {
        'statusCode': 201,
        'body': json.dumps('Alert successfully created.')
    }

lambda_handler(None, None)