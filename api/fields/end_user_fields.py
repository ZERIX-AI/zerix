from flask_restful import fields

# TESTED ON 2024-10-21 09:50 GMT
simple_end_user_fields = {
    "id": fields.String,
    "type": fields.String,
    "is_anonymous": fields.Boolean,
    "session_id": fields.String,
}
