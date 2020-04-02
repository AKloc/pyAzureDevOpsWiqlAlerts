# pyAzureDevOpsWiqlAlerts - dev notes

Cheaty Commands:

- activate venv: source .venv/bin/activate
- deactivate venv: deactivate
- update requirements.txt: pip freeze > requirements.txt
- update function.zip file for AWS upload:
  - in site-packages: zip -r9 function.zip .
  - move file to root, then: zip -r function.zip .

DynamoDB Schema:

- Alert items:

```javascript
    "alert": {
        "alert_name": "string",
        "azure_devops_query": {
            "query_id": "string",
            "query_uri": "http://whatever.com",
            "query_api_token"
        },
        "slack_webhook_ui": "http://slack.com"
    }
```

Per client:

- AzureDevOps URI and Personal Access Token

Local development:

- Create ~/.bash_profile if it doesn't exist
- Add variables for Azure DevOps URI and personal access token
- source ~/.bash_profile