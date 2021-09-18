from datetime import datetime
from flask import (
    jsonify,
)
from app import (
    db,
)
from app.utils.app_functions import (
    serve_otp_signup_email,
    serve_otp_password_email,
)
from app.user.models import (
    User,
)
from app.otp.models import (
    OTP,
)


def generate_otp(user_id, purpose):
    response = {}

    user = db.session.query(User).filter(User.id == user_id).one_or_none()

    if not user:
        response["result"] = False
        response["response"] = "Invalid User ID, Unable to generate OTP"
        return response

    if purpose == 1:
        if user.status is True:
            response["result"] = False
            response["response"] = "User already verified"
            return response
        elif user.status is False:
            response["result"] = False
            response["response"] = "User is blocked, Unable to generate OTP"
            return response

    if (purpose != 1 and purpose != 2):
        response["result"] = False
        response["response"] = "Invalid purpose, Unable to generate OTP"
        return response

    otp = OTP.generate_otp(user_id)

    if not otp:
        response["result"] = False
        response["response"] = "Unable to generate OTP"
        return response

    if purpose == 1:
        serve_otp_signup_email(user.email, otp.otp)
    else:
        serve_otp_password_email(user.email, otp.otp)

    response["result"] = True
    response["response"] = otp.id
    return response


def verify_otp(user_id, otp_id, input_otp):
    response = {}

    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        response["result"] = False
        response["response"] = "Invalid User ID, Unable to verify OTP"
        return response
    elif user.status is False:
        response["result"] = False
        response["response"] = "User is blocked, Unable to verify OTP"
        return response

    otp = db.session.query(OTP).filter(
        OTP.id == otp_id, OTP.created_for == user_id).one_or_none()

    if not otp:
        response["result"] = False
        response["response"] = "Invalid OTP ID, Unable to verify OTP"
        return response
    elif datetime.now() > otp.expiry:
        response["result"] = False
        response["response"] = "OTP Expired, Request a new OTP"
        return response
    elif otp.otp != input_otp:
        response["result"] = False
        response["response"] = "Incorrect OTP, Try Again"
        return response

    response["result"] = True
    return response
