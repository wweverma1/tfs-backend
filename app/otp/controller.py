from datetime import datetime
from flask import (
    jsonify,
    request,
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


def generate_otp(user_id):
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to generate OTP", 400

    purpose = request.args.get('purpose', type=int)
    if (purpose != 1 and purpose != 2):
        return "Invalid purpose, Unable to generate OTP", 400

    otp = OTP.generate_otp(user_id)
    if not otp:
        return "Unable to generate OTP", 400

    if purpose == 1:
        serve_otp_signup_email(user.email, otp.otp)
    else:
        serve_otp_password_email(user.email, otp.otp)
    return jsonify({"id": otp.id}), 200


def verify_otp(otp_id):
    user_id = request.form['user_id']
    input_otp = request.form['input_otp']

    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to verify OTP", 400

    otp = db.session.query(OTP).filter(
        OTP.id == otp_id, OTP.created_for == user_id).one_or_none()
    if not otp:
        return "Invalid OTP ID, Unable to verify OTP", 400
    if datetime.now() > otp.expiry:
        return "OTP Expired, Request a new OTP", 400

    if otp.otp != input_otp:
        return "Incorrect OTP, Try Again", 400
    return "OTP Verified", 200
