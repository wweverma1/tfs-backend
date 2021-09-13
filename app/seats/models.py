# Standard library imports
from datetime import datetime
import traceback

# Related third party imports
from sqlalchemy.exc import SQLAlchemyError

# Local app specific imports
from app import (
    db,
    SCHEMA_NAME,
)


class Seat(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'seat'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    seat_number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.movie.id'))
    screening_id = db.Column(
        db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.screening.id'))
    booking_id = db.Column(
        db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.booking.id'))

    @staticmethod
    def book_seat(seat_number=None, user_id=None, movie_id=None, screening_id=None, booking_id=None):
        try:
            booked_seat = Seat(
                created_at=datetime.now(),
                seat_number=seat_number,
                user_id=user_id,
                movie_id=movie_id,
                screening_id=screening_id,
                booking_id=booking_id
            )
            db.session.add(booked_seat)
            db.session.commit()
            return booked_seat
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
