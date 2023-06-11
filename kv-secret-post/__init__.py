import logging, json

import azure.functions as func
from services.kv_secrets_service import get_kv_secret_by_key


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        raise Exception(f'Error parsing request ${req}')

    request_key = req_body.get('key')
    logging.log('req body carries key: %s' % request_key)
    data = get_kv_secret_by_key(request_key)

    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})