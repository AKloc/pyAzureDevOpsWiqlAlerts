#! python3
from pyAzureDevOpsWiqlAlerts.utilities.azuredevopsinterface import AzureDevopsInterface
from pyAzureDevOpsWiqlAlerts.utilities.slackinterface import SlackInterface


class Alert:

    def __init__(self, alert_name, slack_webhook_uri):
        print('Building alert.')
        self._alert_name = alert_name
        self._slack_webhook_uri = slack_webhook_uri
        self._slack_interface = SlackInterface(self._slack_webhook_uri)

    @property
    def alert_name(self):
        return self._alert_name

    @alert_name.setter
    def alert_name(self, value):
        self._alert_name = value

    @property
    def azure_devops_query_config(self):
        return self._azure_devops_query_config

    @azure_devops_query_config.setter
    def azure_devops_query_config(self, value):
        if 'api_token' in value and 'query_id' in value \
                and 'query_uri' in value:
            self._azure_devops_query_config = value
            self._azure_devops_interface = AzureDevopsInterface(
                uri=self._azure_devops_query_config['query_uri'],
                personal_access_token=self._azure_devops_query_config['api_token']
            )
        else:
            raise ValueError('api_token, query_id, and query_uri \
                must be defined in the dictionary.')

    @property
    def slack_webhook_uri(self):
        return self._slack_webhook_uri

    @slack_webhook_uri.setter
    def slack_webhook_uri(self, value):
        self._slack_webhook_uri = value
        self._slack_interface = SlackInterface(self._slack_webhook_uri)

    def process(self, message):
        self._slack_interface.send_message(message=message, channel=None)
