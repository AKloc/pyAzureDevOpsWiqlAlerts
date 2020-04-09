#! python3

class alert:

    def __init__(self, alert_name):
        print('constructing.')
        self._alert_name = alert_name

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
            and 'query_id' in value:
            self._azure_devops_query_config = value
        else:
            raise ValueError('api_token, query_id, and query_uri \
                must be defined in the dictionary.')
        
    @property
    def slack_webhook_uri(self):
        return self._slack_webhook_uri

    @slack_webhook_uri.setter
    def slack_webhook_uri(self, value):
        self._slack_webhook_uri = value