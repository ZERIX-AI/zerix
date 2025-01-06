from flask_restful import Resource, reqparse

from controllers.console import api
from controllers.console.setup import setup_required
from controllers.console.wraps import account_initialization_required
from libs.login import login_required, current_user
from services.rating_service import RatingService


def _validate_rating(rating):
    if not isinstance(rating, int):
        raise ValueError("Rating must be an integer.")
    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 to 5.")
    return rating

class RatingApi(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("rating", type=_validate_rating, required=True, location="json")
        parser.add_argument("app_id", type=str, required=False, location="json")
        args = parser.parse_args()

        avg_rating = RatingService.update_rating(args["rating"], args["app_id"], current_user.id)

        return float(avg_rating), 200


api.add_resource(RatingApi, "/rating/update")