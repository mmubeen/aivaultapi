from azure.core.exceptions import ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient, KeyVaultSecret
import os


def get_kv_secret_by_key(secret_key) -> str:
    credential = DefaultAzureCredential()
    key_vault_url = os.getenv("KEY_VAULT_URL")

    try:
        secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    except ResourceNotFoundError as e:
        raise KeyVaultNotFoundError(f'Key vault <${key_vault_url}> not found ')

    try:
        key_vault_secret: KeyVaultSecret = secret_client.get_secret(secret_key)
    except ResourceNotFoundError as e:
        raise KeyVaultSecretNotFoundError(f'Key vault value for <${secret_key}> not found ')
    return key_vault_secret.value


class KeyVaultNotFoundError(Exception):
    """Raised when key vault is not found"""
    pass


class KeyVaultSecretNotFoundError(Exception):
    """Raised when key vault secret is not found"""
    pass
