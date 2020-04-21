#! python3
from .azuredevopsinterface import AzureDevopsInterface
from .slackinterface import SlackInterface
import re


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

    def process(self):
        self._azure_devops_interface = AzureDevopsInterface(
            uri=self._azure_devops_query_config['query_uri'],
            personal_access_token=self._azure_devops_query_config['api_token']
        )

        query_results = self._azure_devops_interface.get_azure_devops_work_items_from_query_id(
            query_id=self._azure_devops_query_config['query_id'])

        # message = f'Ran query \'{self._alert_name}\', returned {str(len(query_results))} results.'

        message = self.format_message(query_results)

        self._slack_interface.send_message(message=message)

    def format_message(self, query_results: {}) -> str:
        # First, get the raw f-strings.
        item_raw: str = self._azure_devops_query_config['formatting_f_string_item']
        formatted_header: str = self._azure_devops_query_config['formatting_f_string_header']
        formatted_footer: str = self._azure_devops_query_config['formatting_f_string_footer']
        formatted_items: str = ''

        formatted_header = formatted_header.replace('{TOTAL_NUM_ITEMS}', {str(len(query_results))})
        formatted_footer = formatted_footer.replace('{TOTAL_NUM_ITEMS}', {str(len(query_results))})

        for result_row in query_results:
            formatted_items += self.substitute_result_values_into_f_string(query_results)

        # substitute strings
        return "derp"

    def substitute_result_values_into_f_string(self, f_string: str, result_row: {}) -> str:

        # Find a curly brace value
        result_value_to_replace = re.search(r"\{(.*?)\}", f_string)
        while result_value_to_replace is not None:
            match = result_value_to_replace.group(0)
            result_value = result_row.get(match[1:-1], '(Value not Found)')
            f_string = f_string.replace(match, result_value)
            result_value_to_replace = re.search(r"\{(.*?)\}", f_string)

        # for each string contains regex {something}
        #   try to replace regex {something} with the value in result_row
        #   if not found, except
        return f_string
