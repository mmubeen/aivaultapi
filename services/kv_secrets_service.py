from azure.core.exceptions import ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os


def get_kv_secret_by_key(secret_key):
    credential = DefaultAzureCredential()
    key_vault_url = os.getenv("KEY_VAULT_URL")


    try:
        secret_client = SecretClient(vault_url=key_vault_url, credential=DefaultAzureCredential())
    except ResourceNotFoundError as e:
        raise Exception(f'Key vault <${key_vault_url}> not found ')

    try:
        secret = secret_client.get_secret(secret_key)
    except ResourceNotFoundError as e:
        raise Exception(f'Key vault value for <${secret_key}> not found ')
    return secret
