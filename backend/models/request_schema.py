from marshmallow import Schema, fields
from marshmallow import ValidationError

class CreateUserRequestSchema(Schema):
    name = fields.String(required=True)


class CreateTransactionRequestSchema(Schema):
    user_id = fields.String(required=True)
    category_id = fields.String(required=True)
    date = fields.DateTime()
    amount = fields.Float(required=True)
    currency = fields.String(required=True)


class SearchTransactionRequestSchema(Schema):
    start_date = fields.DateTime(format="iso", required=True)
    end_date = fields.DateTime(format="iso", required=True)


class CreateCategoryRequestSchema(Schema):
    transaction_type_id = fields.String(required=True)
    type = fields.String(required=True)

class SearchCategoryRequestSchema(Schema):
    searchTerm = fields.String(required=True)
