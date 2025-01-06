import os

from flask import session
from flask_restful import Resource, reqparse

from configs import zerix_config
from libs.helper import str_len
from models.model import ZerixSetup
from services.account_service import TenantService

from . import api
from .error import AlreadySetupError, InitValidateFailedError
from .wraps import only_edition_self_hosted

# tested on 2024-10-12 02:36 GMT
class InitValidateAPI(Resource):
    def get(self):
        init_status = get_init_validate_status()
        if init_status:
            return {"status": "finished"}
        return {"status": "not_started"}

    @only_edition_self_hosted
    def post(self):
        # is tenant created
        tenant_count = TenantService.get_tenant_count()
        if tenant_count > 0:
            raise AlreadySetupError()

        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str_len(30), required=True, location="json")
        input_password = parser.parse_args()["password"]

        if input_password != os.environ.get("INIT_PASSWORD"):
            session["is_init_validated"] = False
            raise InitValidateFailedError()

        session["is_init_validated"] = True
        return {"result": "success"}, 201


def get_init_validate_status():
    if zerix_config.EDITION == "SELF_HOSTED":
        if os.environ.get("INIT_PASSWORD"):
            return session.get("is_init_validated") or ZerixSetup.query.first()

    return True


api.add_resource(InitValidateAPI, "/init")
