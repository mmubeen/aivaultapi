import unittest
from unittest import mock
from unittest.mock import patch, MagicMock

from azure.core.exceptions import ResourceNotFoundError, ServiceRequestError

from services.kv_secrets_service import get_kv_secret_by_key, KeyVaultServiceError, KeyVaultSecretNotFoundError
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

    @patch("azure.keyvault.secrets.SecretClient")
    @patch("os.getenv")
    @patch("azure.identity.DefaultAzureCredential")
    def test_get_kv_secret_by_key_key_vault_not_found(self, mock_credential: MagicMock, mock_get_env: MagicMock, mock_client: MagicMock):
        with patch("azure.keyvault.secrets.SecretClient") as mock_function:
            mock_client.raiseError.side_effect = self.service_not_found_side_effect
            _ = get_kv_secret_by_key("key1")
            self.assertRaises(KeyVaultServiceError)

    @patch("os.getenv")
    @patch("azure.identity.DefaultAzureCredential")
    def test_get_kv_secret_by_key_key_vault_service(self, mock_credential: MagicMock, mock_get_env: MagicMock):
        with patch.object(SecretClient, "get_secret") as mock_function:
            mock_function.raiseError.side_effect = self.service_not_found_side_effect
            _ = get_kv_secret_by_key("key1")
            self.assertRaises(KeyVaultServiceError)

    @patch("os.getenv")
    @patch("azure.identity.DefaultAzureCredential")
    def test_get_kv_secret_by_key_key_not_found(self, mock_credential: MagicMock, mock_get_env: MagicMock):
        with patch.object(SecretClient, "get_secret") as mock_function:
            mock_function.raiseError.side_effect = self.resource_not_found_side_effect
            _ = get_kv_secret_by_key("key1")
            self.assertRaises(KeyVaultSecretNotFoundError)

    def resource_not_found_side_effect():
        raise ResourceNotFoundError()

    def service_not_found_side_effect():
        raise ServiceRequestError()
