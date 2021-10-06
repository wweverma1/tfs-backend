# Standard library imports
import traceback
import os
import json
from sqlalchemy.exc import SQLAlchemyError

from flask import (
    jsonify,
    request,
)

# Local app specific imports
from app import (
    db,
)

from app.bookings.models import (
    Booking,
)

from app.user.models import (
    User,
)

from app.movies.models import (
    Movie,
    Screening,
)

from app.seats.models import (
    Seat,
)

from app.bookings.validators import (
    CreateBookingSchema,
)


def create_booking():
    err = CreateBookingSchema().validate(request.get_json())
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    post_data = request.get_json()
    user_id = post_data['user_id']
    movie_id = post_data['movie_id']
    screening_id = post_data['screening_id']
    number_seats = post_data['number_seats']
    seats = post_data['seats']

    user = db.session.query(User.name, User.status, User.number_booking).filter(
        User.id == user_id).one_or_none()
    if not user:
        return "Invalid User Id, Unable to create Booking", 400
    elif user.status is False:
        return "User is Blocked, Can't create Booking", 400
    elif user.status is None:
        return "Complete Your Registration to create Booking", 400
    user_name = user.name

    movie = db.session.query(Movie.name).filter(
        Movie.id == movie_id).one_or_none()
    if not movie:
        return "Invalid Movie Id, Unable to create Booking", 400
    movie_name = movie.name

    screening = db.session.query(Screening.timing).filter(
        Screening.id == screening_id).one_or_none()
    if not screening:
        return "Invalid Screening Id, Unable to create Booking", 400
    screening_time = screening.timing

    if (number_seats != len(seats) or number_seats < 1):
        return "Seat Configuration Mismatch, Unable to Create Booking", 400

    user_seat_limit = os.getenv("USER_SEAT_LIMIT")

    booked_seats = db.session.query(Seat.seat_number).filter(
        Seat.user_id == user_id, Seat.movie_id == movie_id, Seat.screening_id == screening_id).all()
    number_booked_seats = len(booked_seats)
    booked_seats_numbers = [
        booked_seat.seat_number for booked_seat in booked_seats]
    if number_booked_seats + number_seats > user_seat_limit:
        return "Seat Limited Exceeded, Unable to create Booking", 400
    for seat in seats:
        if seat in booked_seats_numbers:
            return "The selected seat is already Taken, Unable to create Booking", 400

    booking = Booking.create_booking(
        user_id, user_name, movie_id, movie_name, screening_id, screening_time, number_seats)
    if not booking:
        return "Error creating Booking", 400
    booking_id = booking.id

    for seat in seats:
        Seat.book_seat(seat, user_id, movie_id, screening_id, booking_id)

    try:
        user.number_booking += 1
        db.session.commit()
        return jsonify({"id": booking_id}), 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Booking created but unable to update user details", 400


def fetch_booking(booking_id):
    booking = db.session.query(Booking).filter(
        Booking.id == booking_id).one_or_none()
    if not booking:
        return "Invalid Bookind ID, Unable to fetch Booking", 400
    if booking.status is False:
        return "Booking Cancelled", 400
    booking_data = {
        "id": booking.id,
        "created_at": booking.created_at,
        "user_id": booking.user_id,
        "user_name": booking.user_name,
        "movie_id": booking.movie_id,
        "movie_name": booking.movie_name,
        "screening_id": booking.screening_id,
        "screening_time": booking.screening_time,
        "number_seats": booking.number_seats,
    }
    return jsonify(booking_data), 200


def cancel_booking(booking_id):
    booking = db.session.query(Booking).filter(
        Booking.id == booking_id).one_or_none()
    if not booking:
        return "Invalid Bookind ID, Unable to fetch Booking", 400
    if booking.status is False:
        return "Booking is already cancelled", 400

    user = db.session.query(User.number_booking).filter(
        User.id == booking.user_id).one_or_none()
    if not user:
        "No User found for this Booking, Unable to cancel", 400

    seats = db.session.query(Seat).filter(Seat.booking_id == booking_id).all()
    try:
        user.number_booking -= 1
        db.session.delete(seats)
        db.session.commit()
        return "Booking Cancelled", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Unable to cancel Booking", 400
