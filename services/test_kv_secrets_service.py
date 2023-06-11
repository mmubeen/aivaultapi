import unittest
from unittest.mock import patch, MagicMock
import responses
import azure.functions as func
from kv_secret_post import main
from services.kv_secrets_service import get_kv_secret_by_key
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class MockingTestTestCase(unittest.TestCase):

    @patch("azure.identity.DefaultAzureCredential")
    @patch("azure.keyvault.secrets.SecretClient")
    def test_get_kv_secret_by_key(self, mock_client: MagicMock, mock_credential: MagicMock):
        mock_client.get_secret.return_value = "value1"
        get_kv_secret_by_key("key1")
