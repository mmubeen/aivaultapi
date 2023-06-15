# Given the client ID and tenant ID for an app registered in Azure,
# provide an Azure AD access token and a refresh token.
import requests
# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.

# pip install msal
from msal import PublicClientApplication, ConfidentialClientApplication, ClientApplication
import sys

# You can hard-code the registered app's client ID and tenant ID here,
# or you can provide them as command-line arguments to this script.
client_id = '955373bc-d80f-4b35-a792-22a8537c059b'
tenant_id = '3e9aadf8-6a16-490f-8dcd-c68860caae0b'
client_secret = "2B08Q~Qa7mE-IrqkS6HyuC9mPpYm01s60u6YnaoD"
application_id = '18edded3-3130-4d99-9ce0-f88dfaa04ebf'

endpoint = 'https://ecf-prod-openai-apim-001.azure-api.net/GetKeyVaultSecret-ECF-PROD/aikey'
ai_endpoint = 'https://ecf-prod-openai-apim-001.azure-api.net/openai/deployments/apim-test-deployment/completions?api-version=2022-12-01'
# Do not modify this variable. It represents the programmatic ID for
# Azure Databricks along with the default scope of '/.default'.
scopes = ['api://18edded3-3130-4d99-9ce0-f88dfaa04ebf/ApiUser.Read']

# Check for too few or too many command-line arguments.
if (len(sys.argv) > 1) and (len(sys.argv) != 3):
    print("Usage: get-tokens.py <client ID> <tenant ID>")
    exit(1)

# If the registered app's client ID and tenant ID are provided as
# command-line variables, set them here.
if len(sys.argv) > 1:
    client_id = sys.argv[1]
    tenant_id = sys.argv[2]

app = ClientApplication(
    client_id=client_id,
    authority="https://login.microsoftonline.com/" + tenant_id,
    client_credential=client_secret
)

acquire_tokens_result = app.acquire_token_by_username_password(username='admin_openai@ecfdata.com',
                                                               password='o1@F}93BMc4.)uq',
                                                               scopes=scopes)

if 'error' in acquire_tokens_result:
    print("Error: " + acquire_tokens_result['error'])
    print("Description: " + acquire_tokens_result['error_description'])
else:
    # print("Access token:\n")
    # print(acquire_tokens_result['access_token'])
    # print("\nRefresh token:\n")
    # print(acquire_tokens_result['refresh_token'])

    header_token = {"Authorization": "Bearer {}".format(acquire_tokens_result['access_token'])}
    # rt = requests.get(url=endpoint, headers=header_token)
    rt = requests.post(url=endpoint, headers=header_token, data=b'{"key":"apimunlimitedkey1"}')
    # print(rt.status_code)
    print(rt.json())

    request_data = b'{"prompt":"Write a product launch email for new AI-powered headphones that are priced at $79.99 and available at Best Buy, Target and Amazon.com. The target audience is tech-savvy music lovers and the tone is friendly and exciting.\n\n1. What should be the subject line of the email?  \n2. What should be the body of the email?","max_tokens":350,"temperature":1,"frequency_penalty":0,"presence_penalty":0,"top_p":1,"stop":null}'

    ai_header_key = {"ocp-apim-subscription-key": "{}".format(rt.json())}

    ai_rt = requests.post(url=endpoint, headers=ai_header_key, data=request_data)

    print(ai_rt.json())
