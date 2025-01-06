from flask_restful import fields

from libs.helper import AppIconUrlField, TimestampField

# TESTED ON 2024-10-21 21:56 GMT
app_fields = {
    "id": fields.String,
    "name": fields.String,
    "mode": fields.String,
    "icon_type": fields.String,
    "icon": fields.String,
    "icon_background": fields.String,
    "icon_url": AppIconUrlField,
    "use_icon_as_answer_icon": fields.Boolean,
}

# TESTED ON 2024-10-21 21:57 GMT
installed_app_fields = {
    "id": fields.String,
    "app": fields.Nested(app_fields),
    "app_owner_tenant_id": fields.String,
    "is_pinned": fields.Boolean,
    "last_used_at": TimestampField,
    "editable": fields.Boolean,
    "uninstallable": fields.Boolean,
}

# TESTED ON 2024-10-21 21:58 GMT
installed_app_list_fields = {"installed_apps": fields.List(fields.Nested(installed_app_fields))}
