# Related third party imports
from marshmallow import (
    Schema,
    fields,
    INCLUDE,
)


class CreateBookingSchema(Schema):
    class Meta:
        unknown = INCLUDE
    user_id = fields.Integer(required=True)
    movie_id = fields.Integer(required=True)
    screening_id = fields.Integer(required=True)
    number_seats = fields.Integer(required=True)
    seats = fields.List(cls_or_instance=fields.Integer(), Required=True)
