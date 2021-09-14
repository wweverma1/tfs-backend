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


class Booking(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.user.id'))
    user_name = db.Column(db.String(100))
    movie_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.movie.id'))
    movie_name = db.Column(db.String(100))
    screening_id = db.Column(
        db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.screening.id'))
    screening_time = db.Column(db.DateTime)
    number_seats = db.Column(db.Integer)

    @staticmethod
    def create_booking(user_id=None, user_name=None, movie_id=None, movie_name=None,
                       screening_id=None, screening_time=None, number_seats=None):
        try:
            booking = Booking(
                created_at=datetime.now(),
                status=True,
                user_id=user_id,
                user_name=user_name,
                movie_id=movie_id,
                movie_name=movie_name,
                screening_id=screening_id,
                screening_time=screening_time,
                number_seats=number_seats,
            )
            db.session.add(booking)
            db.session.commit()
            return booking
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
