# Standard library imports
from datetime import datetime
from datetime import timedelta
import traceback
import random
import string

# Related third party imports
from sqlalchemy.exc import SQLAlchemyError

# Local app specific imports
from app import (
    db,
    SCHEMA_NAME,
)


class OTP(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'otp'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    created_for = db.Column(
        db.Integer, db.ForeignKey(f'{SCHEMA_NAME}.user.id'))
    otp = db.Column(db.String(6))
    expiry = db.Column(db.DateTime)

    @staticmethod
    def generate_otp(user_id=None):
        try:
            otp_size = 6
            code = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                           for n in range(otp_size)])
            otp = OTP(
                created_at=datetime.now(),
                created_for=user_id,
                otp=code,
                expiry=datetime.now() + timedelta(minutes=10),
            )
            db.session.add(otp)
            db.session.commit()
            return otp
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
