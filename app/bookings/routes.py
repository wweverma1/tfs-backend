from flask import Blueprint

from app.bookings.controller import (
    create_booking,
    fetch_booking,
    cancel_booking,
)

bookings_api = Blueprint('bookings', __name__)

bookings_api.add_url_rule(rule='/bookings/create',
                          view_func=create_booking, methods=['POST', ])
bookings_api.add_url_rule(rule='/bookings/<int:booking_id>/fetch',
                          view_func=fetch_booking, methods=['GET', ])
bookings_api.add_url_rule(rule='/bookings/<int:booking_id>/cancel',
                          view_func=cancel_booking, methods=['GET', ])
