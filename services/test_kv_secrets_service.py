import unittest
from unittest.mock import patch, MagicMock
from services.kv_secrets_service import get_kv_secret_by_key
from azure.keyvault.secrets import SecretClient


class MockingTestTestCase(unittest.TestCase):

    @patch("azure.identity.DefaultAzureCredential")
    @patch.object(SecretClient, "get_secret", return_value="value1")
    def test_get_kv_secret_by_key(self, mock_client: MagicMock, mock_credential: MagicMock):
        get_kv_secret_by_key("key1")
