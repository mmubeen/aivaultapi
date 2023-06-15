# Given the client ID and tenant ID for an app registered in Azure,
# provide an Azure AD access token and a refresh token.
import requests
# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.

from msal import ClientApplication
import sys

# You can hard-code the registered app's client ID and tenant ID here,
# or you can provide them as command-line arguments to this script.
client_id = '955373bc-d80f-4b35-a792-22a8537c059b'
tenant_id = '3e9aadf8-6a16-490f-8dcd-c68860caae0b'
client_secret = "TUD8Q~-VbYwGOd4M3J.-9kVUqTn-71E_QdSBVc8D"
application_id = '955373bc-d80f-4b35-a792-22a8537c059b'

endpoint = 'https://regn-eastus-ga-prod-apim-ai-001.azure-api.net/REGN-EastUS-GA-Prod-FA-AI-001/aikey'
ai_endpoint = 'https://regn-eastus-ga-prod-apim-ai-001.azure-api.net/v1/completions'
# Do not modify this variable. It represents the programmatic ID for
# Azure Databricks along with the default scope of '/.default'.
scopes = ['api://955373bc-d80f-4b35-a792-22a8537c059b/ApiUser.Read']

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
    authority="https://login.microsoftonline.com/" + tenant_id
)

acquire_tokens_result = app.acquire_token_by_username_password(username='svc.dte-azopenai@regeneron.com',
                                                               password='pzW3QrAm4?*,PQ7n',
                                                               scopes=scopes)

if 'error' in acquire_tokens_result:
    print("Error: " + acquire_tokens_result['error'])
    print("Description: " + acquire_tokens_result['error_description'])
else:
    header_token = {"Authorization": "Bearer {}".format(acquire_tokens_result['access_token'])}
    rt = requests.post(url=endpoint, headers=header_token, data=b'{"key":"apimunlimitedkey1"}')

    request_data = b'{"prompt":"What should be the body of the email?","max_tokens":350,"temperature":1,"frequency_penalty":0,"presence_penalty":0,"top_p":1,"stop":null}'
    ai_header_key = {"Ocp-Apim-Subscription-Key": "{}".format(rt.json())}
    ai_rt = requests.post(url=ai_endpoint, headers=ai_header_key, data=request_data)

    print(ai_rt.json())
