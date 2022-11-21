from marshmallow import Schema, fields
from marshmallow import ValidationError

class CategorySchema(Schema):
    transaction_type = fields.String()
    transaction_type_id = fields.String()
    type = fields.String()


class GetCategoryRespondSchema(Schema):
    categories = fields.Dict(
        keys=fields.String(),
        values=fields.Nested(CategorySchema))
    success = fields.Boolean()
    total_categories = fields.Integer()
