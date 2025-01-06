from flask_restful import Resource

from configs import zerix_config
from controllers.service_api import api


class IndexApi(Resource):
    def get(self):
        return {
            "welcome": "Zerix OpenAPI",
            "api_version": "v1",
            "server_version": zerix_config.CURRENT_VERSION,
        }


api.add_resource(IndexApi, "/")
