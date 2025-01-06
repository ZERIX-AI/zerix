from flask_restful import fields

from libs.helper import TimestampField

# TESTED ON 2024-10-21 09:55 GMT
document_fields = {
    "id": fields.String,
    "data_source_type": fields.String,
    "name": fields.String,
    "doc_type": fields.String,
}

# TESTED ON 2024-10-21 10:06 GMT
segment_fields = {
    "id": fields.String,
    "position": fields.Integer,
    "document_id": fields.String,
    "content": fields.String,
    "answer": fields.String,
    "word_count": fields.Integer,
    "tokens": fields.Integer,
    "keywords": fields.List(fields.String),
    "index_node_id": fields.String,
    "index_node_hash": fields.String,
    "hit_count": fields.Integer,
    "enabled": fields.Boolean,
    "disabled_at": TimestampField,
    "disabled_by": fields.String,
    "status": fields.String,
    "created_by": fields.String,
    "created_at": TimestampField,
    "indexing_at": TimestampField,
    "completed_at": TimestampField,
    "error": fields.String,
    "stopped_at": TimestampField,
    "document": fields.Nested(document_fields),
}

# TESTED ON 2024-10-21 10:10 GMT
hit_testing_record_fields = {
    "segment": fields.Nested(segment_fields),
    "score": fields.Float,
    "tsne_position": fields.Raw,
}
