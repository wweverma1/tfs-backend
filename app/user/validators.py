# Related third party imports
from operator import eq
from marshmallow import (
    Schema,
    fields,
    validate,
    INCLUDE,
)


class CreateUserSchema(Schema):
    class Meta:
        unknown = INCLUDE
    email = fields.String(required=True, validate=validate.Length(min=10))
    password = fields.String(required=True, validate=validate.Length(min=6))


class CompleteProfileSchema(Schema):
    class Meta:
        unknown = INCLUDE
    first_name = fields.String(required=True, validate=validate.Length(min=3))
    last_name = fields.String(required=True, validate=validate.Length(min=3))
    phone = fields.String(required=True, validate=validate.Length(equal=10))
    notifications = fields.Boolean(required=True)
