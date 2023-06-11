# <project_root>/tests/test_my_second_function.py
import unittest
from unittest.mock import patch
import responses
import azure.functions as func
from kv_secret_post import main


class MockingTestTestCase(unittest.TestCase):
    @responses.activate
    @patch("services.kv_secrets_service.get_kv_secret_by_key")
    def test_kv_secret_post(self, mock_get_secret):
        # Construct a mock HTTP request.
        responses.add(**{
            'method': responses.POST,
            'url': 'https://example.com/api/kv_secret_post',
            'body': '{"key": "key1"}',
            'status': 200,
            'content_type': 'application/json',
            'adding_headers': {'X-Foo': 'Bar'}
        })
        req = func.HttpRequest(method="POST", url="https://example.com/api/kv_secret_post",
                               body='{"key": "key1"}'.encode(encoding="UTF8"))
        # test_mock.return_value = "value1"
        # Call the function.

        mock_get_secret.return_value = "value1"
        resp = main(req)

        # Check the output.
        self.assertEqual(resp.get_body(), b'"value1"')
