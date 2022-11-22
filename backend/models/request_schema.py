from marshmallow import Schema, fields
from marshmallow import ValidationError

class CreateCategoryRequestSchema(Schema):
    transaction_type_id = fields.String(required=True)
    type = fields.String(required=True)


class CreateTransactionRequestSchema(Schema):
    category_id = fields.String(required=True)
    date = fields.DateTime()
    amount = fields.Float(required=True)
    currency = fields.String(required=True)
    note = fields.String()


class UpdateCategoryRequestSchema(Schema):
    transaction_type_id = fields.String(required=True)
    type = fields.String(required=True)


class UpdateTransactionRequestSchema(Schema):
    category_id = fields.String(required=True)
    date = fields.DateTime()
    amount = fields.Float(required=True)
    currency = fields.String(required=True)
    note = fields.String()

class SearchCategoryRequestSchema(Schema):
    searchTerm = fields.String(required=True)


class SearchTransactionRequestSchema(Schema):
    start_date = fields.DateTime(format="iso", required=True)
    end_date = fields.DateTime(format="iso", required=True)