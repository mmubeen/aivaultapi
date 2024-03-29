from azure.core.exceptions import ResourceNotFoundError, ServiceRequestError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient, KeyVaultSecret
import os


def get_kv_secret_by_key(secret_key) -> str:
    credential = DefaultAzureCredential()
    key_vault_url = os.getenv("KEY_VAULT_URL")

    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

    try:
        key_vault_secret: KeyVaultSecret = secret_client.get_secret(secret_key)
    except ServiceRequestError as e:
        raise KeyVaultServiceError(f'Key vault <${key_vault_url}> not found ')
    except ResourceNotFoundError as e:
        raise KeyVaultSecretNotFoundError(f'Key vault value for <${secret_key}> not found ')
    return key_vault_secret.value


class KeyVaultServiceError(Exception):
    """Raised when key vault is not found"""
    pass


class KeyVaultSecretNotFoundError(Exception):
    """Raised when key vault secret is not found"""
    pass
