from flask_restful import Resource

from configs import zerix_config
from . import api


class VersionApi(Resource):
    def get(self):
        return {
            "version": zerix_config.CURRENT_VERSION,
            "release_date": "2024-10-28",
            "release_notes": "https://docs.zerix.io/",
        }

api.add_resource(VersionApi, "/version")
