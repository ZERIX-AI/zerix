import logging

from extensions.ext_database import db
from models.model import Rating, AppExtension

logger = logging.getLogger(__name__)

class RatingService:

    @staticmethod
    def update_rating(rating_value, app_id, user_id):
        rating = Rating.query.filter_by(app_id=app_id, user_id=user_id).first()
        if not rating:
            rating = Rating(app_id=app_id, user_id=user_id, rating=rating_value)
            db.session.add(rating)
        else:
            rating.rating = rating_value

        # update app avg rating
        avg_rating = db.session.query(db.func.avg(Rating.rating)).filter_by(app_id=app_id).scalar()
        app_extension = AppExtension.query.filter_by(id=app_id).first()
        if app_extension:
            app_extension.rating = avg_rating
        else:
            app_extension = AppExtension(id=app_id, rating=avg_rating)

        db.session.add(app_extension)
        db.session.commit()
        return avg_rating
