from flask_restful import fields

from libs.helper import TimestampField

simple_account_fields = {"id": fields.String, "name": fields.String, "email": fields.String}

# TESTED ON 2024-10-21 22:05 GMT
account_fields = {
    "id": fields.String,
    "name": fields.String,
    "address": fields.String,
    "avatar": fields.String,
    "email": fields.String,
    "is_password_set": fields.Boolean,
    "interface_language": fields.String,
    "interface_theme": fields.String,
    "timezone": fields.String,
    "last_login_at": TimestampField,
    "last_login_ip": fields.String,
    "created_at": TimestampField,
}

# TESTED ON 2024-10-21 22:07 GMT
account_with_role_fields = {
    "id": fields.String,
    "name": fields.String,
    "avatar": fields.String,
    "email": fields.String,
    "last_login_at": TimestampField,
    "last_active_at": TimestampField,
    "created_at": TimestampField,
    "role": fields.String,
    "status": fields.String,
}

# TESTED ON 2024-10-21 22:08 GMT
account_with_role_list_fields = {"accounts": fields.List(fields.Nested(account_with_role_fields))}
