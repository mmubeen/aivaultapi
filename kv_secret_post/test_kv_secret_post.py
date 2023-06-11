import unittest
from unittest.mock import patch
import responses
import azure.functions as func
from kv_secret_post import main
from services.kv_secrets_service import KeyVaultServiceError, KeyVaultSecretNotFoundError


class MockingTestCase(unittest.TestCase):
    @responses.activate
    @patch("services.kv_secrets_service.get_kv_secret_by_key")
    def test_kv_secret_post(self, mock_get_secret):
        # Construct a mock HTTP request.
        req = func.HttpRequest(method="POST", url="https://example.com/api/kv_secret_post",
                               body='{"key": "key1"}'.encode(encoding="UTF8"))
        # Call the function.
        mock_get_secret.return_value = "value1"
        resp = main(req)

        # Check the output.
        self.assertEqual(resp.get_body(), b'"value1"')

    # @responses.activate
    # @patch("services.kv_secrets_service.get_kv_secret_by_key")
    # def test_kv_secret_key_service_error(self, mock_get_secret):
    #     # Construct a mock HTTP request.
    #     responses.add(**{
    #         'method': responses.POST,
    #         'url': 'https://example.com/api/kv_secret_post',
    #         'body': '{"key": "key1"}',
    #         'status': 200,
    #         'content_type': 'application/json',
    #         'adding_headers': {'X-Foo': 'Bar'}
    #     })
    #     req = func.HttpRequest(method="POST", url="https://example.com/api/kv_secret_post",
    #                            body='{"key": "key1"}'.encode(encoding="UTF8"))
    #     # Call the function.
    #     mock_get_secret.side_effect = self.service_error_side_effect()
    #     resp = main(req)
    #     self.assertRaises(KeyVaultServiceError)
    #
    # def service_error_side_effect(self):
    #     raise KeyVaultServiceError()
    #
    # def key_not_found_side_effect(self):
    #     raise KeyVaultSecretNotFoundError()