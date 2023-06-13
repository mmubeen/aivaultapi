import requests
import json

def get_token(auth_url, client_id, scope, client_secret, grant_type = 'client_credentials'):
    """
     return: tuple dict with access_token, status_code
        {'access_token': 'tokenid'
        'expires_in': 3600,
        'ext_expires_in': 0,
        'token_type': 'Bearer'}, 200
    """
    # Request access token:
    # https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url =auth_url
    data = { "client_id": client_id,
            "scope": scope,
            "client_secret": client_secret,
            "grant_type": grant_type
        }
    # requests doc http://docs.python-requests.org/en/v0.10.7/user/quickstart/#custom-headers
    r = requests.post(url=url, data=data, headers=headers)

    return r.json(), r.status_code

# Change these vars to test:
auth_url = 'https://login.microsoftonline.com/7d5a8898-6564-4329-9289-c87046c026ef/oauth2/v2.0/token'
client_id = '37d5eb41-d3a7-4995-bb4b-29d4f9f2db2e'
scope = 'api://37d5eb41-d3a7-4995-bb4b-29d4f9f2db2e/.default'
client_secret = "NX.8Q~jnAl_9sYQAWRphVPsv9QtBIwS~PuRAGdr~"


url_check = 'https://ai-apim.azure-api.net/aivaultapi/tasks'
get_token = get_token(auth_url, client_id, scope, client_secret)
access_token = get_token[0]['access_token']
print(access_token)
header_token = {"Authorization": "Bearer {}".format(access_token)}
rt = requests.get(url=url_check, headers=header_token)
print(rt.status_code)
print(rt.json())