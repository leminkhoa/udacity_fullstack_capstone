from marshmallow import Schema, fields, ValidationError
from marshmallow import ValidationError

class CreateUserRequestSchema(Schema):
    name = fields.String(required=True)


class CreateTransactionRequestSchema(Schema):
    user_id = fields.String(required=True)
    category_id = fields.String(required=True)
    date = fields.DateTime()
    amount = fields.Float(required=True)
    currency = fields.String(required=True)

class CreateCategoryRequestSchema(Schema):
    transaction_type_id = fields.String(required=True)
    type = fields.String(required=True)