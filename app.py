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
# auth_url = 'https://login.microsoftonline.com/7d5a8898-6564-4329-9289-c87046c026ef/oauth2/v2.0/token'
auth_url = 'https://login.microsoftonline.com/3e9aadf8-6a16-490f-8dcd-c68860caae0b/oauth2/v2.0/token'
client_id = '18edded3-3130-4d99-9ce0-f88dfaa04ebf'
scope = 'api://18edded3-3130-4d99-9ce0-f88dfaa04ebf/ApiUser.Read'
client_secret = "2B08Q~Qa7mE-IrqkS6HyuC9mPpYm01s60u6YnaoD"


# client_id = 'bd01c2aa-22e4-404e-8ddf-a0425166d632'
# scope = 'api://bd01c2aa-22e4-404e-8ddf-a0425166d632/.default'
# client_secret = "Gm28Q~koyfbmz1ts_XxG7ukgKVPVUZhEzXPekbR3"


# url_check = 'https://ai-apim.azure-api.net/aivaultapi/tasks'
url_check = 'https://regn-eastus-ga-prod-apim-ai-001.azure-api.net/REGN-EastUS-GA-Prod-FA-AI-001/tasks'
get_token, _ = get_token(auth_url, client_id, scope, client_secret, 'authorization_code')
print(get_token)
access_token = get_token[0]['access_token']
print(access_token)
header_token = {"Authorization": "Bearer {}".format(access_token)}
rt = requests.get(url=url_check, headers=header_token)
print(rt.status_code)
print(rt.json())