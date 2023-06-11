import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from services.kv_secrets_service import get_kv_secret_by_key
from azure.keyvault.secrets import SecretClient


class MockingTestTestCase(unittest.TestCase):

    @patch("os.getenv")
    @patch("azure.identity.DefaultAzureCredential")
    def test_get_kv_secret_by_key(self, mock_credential: MagicMock, mock_get_env: MagicMock):
        with patch.object(SecretClient, "get_secret") as mock_function:
            key_vault_secret = mock.MagicMock()
            key_vault_secret.value = "value1"
            mock_function.return_value = key_vault_secret
            result = get_kv_secret_by_key("key1")
            self.assertEqual(result, "value1")
