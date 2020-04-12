# pyAzureDevOpsWiqlAlerts - Development Notes

## Noob Command Reminders

- To create a python virtual environment: ```source .venv/bin/activate```
- Deactivate python venv: ```deactivate```
- To update requirements.txt: ```pip freeze > requirements.txt```
- Creating function.zip file for AWS upload:
  - in site-packages: ```zip -r9 function.zip .```
  - move file to root, then: ```zip -r function.zip .```

## DynamoDB Schema

- Alert items:

```javascript
    {
        "alerts": [{
            "alert_name": "string",
            "azure_devops_query": {
                "query_id": "string",
                "query_uri": "http://whatever.com",
                "api_token": "token"
            },
            "cron_schedule": "cron",
            "slack_webhook_ui": "http://slack.com",
            "formatting_f_string_header": "something something something",
            "formatting_f_string_item": "something something something",
            "formatting_f_string_footer": "something something something"
        }]
    }
```

## Local development

### Creating Environment Variables

- Create ~/.bash_profile if it doesn't exist
- Add environment variables for azure_devops_access_token, azure_devops_uri, aws_access_key, aws_secret_access_key
- ```source ~/.bash_profile```