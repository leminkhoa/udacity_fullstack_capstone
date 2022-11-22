from marshmallow import Schema, fields
from marshmallow import ValidationError

class CategorySchema(Schema):
    transaction_type = fields.String()
    transaction_type_id = fields.String()
    type = fields.String()


class GetCategoryRespondSchema(Schema):
    categories = fields.Dict(
        keys=fields.String(),
        values=fields.Nested(CategorySchema)
    )
    success = fields.Boolean()
    total_categories = fields.Integer()


class TransactionSchema(Schema):
    id = fields.String()
    category_id = fields.String(allow_none=True)
    date = fields.String()
    amount = fields.Float()
    currency = fields.String()
    note = fields.String()


class GetTransactionRespondSchema(Schema):
    transactions = fields.List(fields.Nested(TransactionSchema))
    success = fields.Boolean()
    total_transactions = fields.Integer()
