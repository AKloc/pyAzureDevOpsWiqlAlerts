# pyAzureDevOpsWiqlAlerts
Tool to send messages based on "hits" from Azure Dev Ops WIQL reports. e.g.: Write a WIQL that queries for bugs that are over one day old, plug it into this tool, tool queries the reports at a scheduled interval and spits out results. Built in Python, hosted in AWS Lambda.

MVP:
- Grab reports, basic formatting, and ADO credentials from cloud configuration
- Output to Slack

Grandiose Plans:
- Add configuration to a CosmosDB
  - Interval
  - Report
  - f-string style formatting
- React.js configurator!
- Query Jira
- Query stored procs
