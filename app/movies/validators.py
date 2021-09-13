# Related third party imports
from marshmallow import (
    Schema,
    fields,
    validate,
    INCLUDE,
)


class CreateMovieSchema(Schema):
    class Meta:
        unknown = INCLUDE
    name = fields.String(required=True, validate=validate.Length(min=1))
    lang = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    duration = fields.Integer(required=False)
    is_blockbuster = fields.Boolean(required=True)
    poster_url = fields.String(required=False)
    trailer_url = fields.String(required=False)


class CreateScreeningSchema(Schema):
    class Meta:
        unknown = INCLUDE
    timing = fields.DateTime(required=True)
