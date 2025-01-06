from flask_restful import Resource

from controllers.console import api

# tested on 2024-10-12 02:42 GMT
class PingApi(Resource):
    def get(self):
        """
        For connection health check
        """
        return {"result": "pong"}


api.add_resource(PingApi, "/ping")
