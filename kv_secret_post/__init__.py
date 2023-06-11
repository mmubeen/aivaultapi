import logging, json
from http import HTTPStatus

import azure.functions as func
import services.kv_secrets_service


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY)

    request_key = req_body.get('key')
    logging.info('req body carries key: %s' % request_key)
    try:
        data = services.kv_secrets_service.get_kv_secret_by_key(request_key)
        return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
    except services.kv_secrets_service.KeyVaultSecretNotFoundError as e:
        return func.HttpResponse(status_code=HTTPStatus.NOT_FOUND)
    except services.kv_secrets_service.KeyVaultServiceError as e:
        return func.HttpResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY)

