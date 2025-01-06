from flask_restful import fields

from libs.helper import TimestampField

# TESTED ON 2024-10-21 09:52 GMT
upload_config_fields = {
    "file_size_limit": fields.Integer,
    "batch_count_limit": fields.Integer,
    "image_file_size_limit": fields.Integer,
}

# TESTED ON 2024-10-21 09:53 GMT
file_fields = {
    "id": fields.String,
    "name": fields.String,
    "size": fields.Integer,
    "extension": fields.String,
    "mime_type": fields.String,
    "created_by": fields.String,
    "created_at": TimestampField,
}
