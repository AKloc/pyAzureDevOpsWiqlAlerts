#!python3
import json
import os
from pyAzureDevOpsWiqlAlerts.utilities import azuredevopsinterface


def lambda_handler(event, context):
    # Fetch AWS environment variables
    if 'AZURE_DEVOPS_URI' in os.environ.keys():
        azure_devops_uri = os.environ['AZURE_DEVOPS_URI']
    else:
        azure_devops_uri = 'no uri set'

    if 'AZURE_DEVOPS_ACCESS_TOKEN' in os.environ.keys():
        azure_devops_access_token = os.environ['AZURE_DEVOPS_ACCESS_TOKEN']
    else:
        azure_devops_access_token = 'no access token set'

    f = azuredevopsinterface(azure_devops_uri, azure_devops_access_token)
    f.passthrough_method('Derp')

    f.get_azure_devops_work_items_from_query_id( \
        query_id='705fc4ed-11f7-41f1-bdf0-e3f0197a4598')

    return {
        'statusCode': 200,
        'body': json.dumps('azure_devops_interface did stuff.')
    }


lambda_handler(None, None)
