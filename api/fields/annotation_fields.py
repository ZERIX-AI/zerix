from flask_restful import fields

from libs.helper import TimestampField

# TESTED ON 2024-10-20 02:56 GMT
annotation_fields = {
    "id": fields.String,
    "question": fields.String,
    "answer": fields.Raw(attribute="content"),
    "hit_count": fields.Integer,
    "created_at": TimestampField,
    # 'account': fields.Nested(simple_account_fields, allow_null=True)
}

# TESTED ON 2024-10-20 03:18 GMT
annotation_list_fields = {
    "data": fields.List(fields.Nested(annotation_fields)),
}

# TESTED ON 2024-10-20 03:22 GMT
annotation_hit_history_fields = {
    "id": fields.String,
    "source": fields.String,
    "score": fields.Float,
    "question": fields.String,
    "created_at": TimestampField,
    "match": fields.String(attribute="annotation_question"),
    "response": fields.String(attribute="annotation_content"),
}

# TESTED ON 2024-10-20 03:29 GMT
annotation_hit_history_list_fields = {
    "data": fields.List(fields.Nested(annotation_hit_history_fields)),
}
