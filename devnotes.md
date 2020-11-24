# pyAzureDevOpsWiqlAlerts - Development Notes

## Noob Command Reminders

- To create a python virtual environment: ```source .venv/bin/activate```
- Deactivate python venv: ```deactivate```
- To update requirements.txt: ```pip freeze > requirements.txt```
- Creating function.zip file for AWS upload:
  - in site-packages: ```zip -r9 function.zip .```
  - move file to pyAzureDevOpsWiqlAlerts (not the root), then: ```zip -r function.zip .```

## DynamoDB Schema

- Alert items:

```javascript
{
  "alert_name": "Refined Tickets Notification",
  "azure_devops_query": {
    "api_token": "y",
    "query_id": "705fc4ed-11f7-41f1-bdf0-e3f0197a4598",
    "query_uri": "https://dev.azure.com/x"
  },
  "cron_schedule": "cron",
  "enabled": false,
  "f_string_footer": "Here's the footer. Total number of items = {TOTAL_NUM_ITEMS}",
  "f_string_header": "Here's the header. Total number of items = {TOTAL_NUM_ITEMS}",
  "f_string_item": "Here's an item. Title: {System.Title} ID: {System.ID} WorkItemType: {System.WorkItemType}",
  "owner": "Weyland Yutani",
  "slack_webhook_uri": "https://hooks.slack.com/services/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"
}
```

##

### Supported variables for substitutions:

- {TOTAL_NUM_ITEMS}: The total number of rows returned by the query. Works in any field.
- {fieldname}: Displays the value for the current item for the specified fieldname. Works only in the "formatting_f_string_item" field.

## Local development

### Creating Environment Variables

- Create ~/.bash_profile if it doesn't exist
- Add environment variables for azure_devops_access_token, azure_devops_uri, aws_access_key, aws_secret_access_key
- ```source ~/.bash_profile```
