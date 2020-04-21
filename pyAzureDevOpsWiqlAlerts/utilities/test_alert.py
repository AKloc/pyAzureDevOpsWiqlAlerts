import unittest
from pyAzureDevOpsWiqlAlerts.utilities.alert import Alert


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._alert_under_test = Alert(alert_name='alert_name', slack_webhook_uri='uri')

    def test_azure_devops_query_config_setter_with_required_parameters(self):
        config = {
            'api_token': 'test',
            'query_id': 'test',
            'query_uri': 'http://www.google.com'
        }

        try:
            self._alert_under_test.azure_devops_query_config = config
        except Exception:
            self.fail()

    def test_azure_devops_query_config_setter_without_required_parameters(self):

        config = {}
        with self.assertRaises(ValueError):
            self._alert_under_test.azure_devops_query_config = config

        config = {
            'query_id': 'test',
            'query_uri': 'http://www.google.com'
        }
        with self.assertRaises(ValueError):
            self._alert_under_test.azure_devops_query_config = config

        config = {
            'api_token': 'test',
            'query_id': 'test'
        }
        with self.assertRaises(ValueError):
            self._alert_under_test.azure_devops_query_config = config

        config = {
            'query_id': 'test',
            'query_uri': 'http://www.google.com'
        }
        with self.assertRaises(ValueError):
            self._alert_under_test.azure_devops_query_config = config

    def test_substitute_result_values_into_f_string_with_valid_substitutions(self):

        f_string = 'TEST {System.Title}, {TestValue}, Check'
        result_row = {
            'System.Title': 'Title',
            'TestValue': 'Some test value'
        }

        expected_value = 'TEST Title, Some test value, Check'
        actual_value = self._alert_under_test.substitute_result_values_into_f_string(f_string, result_row)

        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
