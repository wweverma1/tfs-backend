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


class User(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    status = db.Column(db.Boolean, nullable=True)
    user_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10), unique=True, nullable=True)
    roll_number = db.Column(db.String(10), nullable=True)
    pswd = db.Column(db.LargeBinary)
    number_booking = db.Column(db.Integer, nullable=True)
    notifications = db.Column(db.Boolean, nullable=True)

    @staticmethod
    def create_user(email=None, password=None):
        try:
            user = User(
                created_at=datetime.now(),
                status=None,
                email=email,
                pswd=password,
            )
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
