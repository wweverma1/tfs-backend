from datetime import datetime

# Standard library imports
import bcrypt
import json
import traceback
from sqlalchemy.exc import SQLAlchemyError

from flask import (
    jsonify,
    request,
)

# Local app specific imports
from app import (
    db,
)

from app.user.models import (
    User,
)

from app.otp.models import (
    OTP,
)

from app.otp.controller import (
    generate_otp,
    verify_otp,
)

from app.user.validators import (
    CreateUserSchema,
    CompleteProfileSchema,
)


def create_user_account():
    err = CreateUserSchema().validate(request.form)
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    email = request.form['email']
    password = request.form['password']

    existing_user_count = User.query.filter_by(email=email).count()
    if existing_user_count != 0:
        return "A User already exists with this email address", 400

    hashed_p = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User.create_user(email, hashed_p)
    if not user:
        return "Error creating User", 400

    # purpose = 1 for verifying email
    otp = generate_otp(user.id, 1)
    if otp['result'] is False:
        return otp['response'], 400

    return jsonify({"user_id": user.id, "otp_id": otp['response']}), 200


def user_login():
    err = CreateUserSchema().validate(request.form)
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    email = request.form['email']
    password = request.form['password']

    user = db.session.query(User).filter(User.email == email).one_or_none()
    if not user:
        return "No user exists with this email address", 400

    if bcrypt.checkpw(password.encode('utf-8'), user.pswd):
        if user.status is True:
            return jsonify({"action": 1}), 200
        elif user.status is None:
            return jsonify({"action": 2}), 200
        else:
            return "User is Blocked, Unable to Login", 400
    else:
        return "Incorrect Password, Unable to Login", 400


def verify_user_email(user_id):
    purpose = request.args.get('purpose', type=int, default=1)
    otp_id = request.form['otp_id']
    input_otp = request.form['otp']

    otp = verify_otp(user_id, otp_id, input_otp)
    if otp['result'] is False:
        return otp['response'], 400

    if purpose == 1:
        return jsonify({"action": 2}), 200
    else:
        return jsonify({"user_id": user_id}), 200


def complete_user_profile(user_id):
    err = CompleteProfileSchema().validate(request.form)
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    notifications = True if request.form['notifications'] == "True" else False

    if any(char.isdigit() for char in first_name):
        return "Invalid Name, Can't Complete User Profile", 400
    if any(char.isdigit() for char in last_name):
        return "Invalid Name, Can't Complete User Profile", 400
    name = first_name + ' ' + last_name

    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to complete User profile", 400
    elif user.status is True:
        return "User Profile is already completed", 400
    elif user.status is False:
        return "User is Blocked, Unable to complete User Profile", 400

    try:
        user.user_name = name
        user.phone = phone
        user.notifications = notifications
        if 'roll_number' in request.form:
            user.roll_number = request.form['roll_number']
        user.status = True
        user.number_booking = 0
        db.session.commit()
        return "User Profile Completed", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Complete User Profile", 400


def update_user_profile(user_id):
    phone = request.form['phone']
    notifications = True if request.form['notifications'] == "True" else False

    if len(phone) != 10:
        return "Invalid Phone Number, Unable to update User Profile", 400

    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to complete User profile", 400
    elif user.status is None:
        return "User Profile is not completed, Unable to update User Profile", 400
    elif user.status is False:
        return "User is Blocked, Unable to update User Profile", 400

    try:
        user.phone = phone
        user.notifications = notifications
        db.session.commit()
        return "User Profile Updated", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Update User Profile", 400


def update_user_password(user_id):
    current_pswd = request.form['password']
    new_pswd = request.form['new_password']

    if len(new_pswd) < 6:
        return "Password must be atleast 6 characters long", 400
    hashed_p = bcrypt.hashpw(new_pswd.encode('utf-8'), bcrypt.gensalt())

    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to change password", 400

    if not bcrypt.checkpw(current_pswd.encode('utf-8'), user.pswd):
        return "Incorrect current Password", 400

    try:
        user.pswd = hashed_p
        db.session.commit()
        return "Password changed", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't change Password", 400


def fetch_user_profile(user_id):
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to fetch User", 400

    user_data = {
        "user_id": user.id,
        "joined_on": user.created_at,
        "status": "Active" if user.status is True else "Incomplete" if user.status is None else "Blocked",
        "name": user.user_name,
        "email": user.email,
        "phone": user.phone,
        "roll_number": user.roll_number,
        "number_bookings": user.number_booking,
    }
    return jsonify(user_data), 200


def block_unblock_user(user_id):
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        return "Invalid User ID, Unable to change Status", 400

    try:
        if (user.status is True or user.status is None):
            action = "Blocked"
            user.status = False
        else:
            action = "Unblocked"
            user.status = True
        db.session.commit()
        return "User " + action, 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't change Status", 400


def reset_user_password():
    email = request.form['email']

    user = db.session.query(User).filter(User.email == email).one_or_none()
    if not user:
        return "No account linked to this email address", 400

    # purpose = 2 for resetting password
    otp = generate_otp(user.id, 2)
    if otp['result'] is False:
        return otp['response'], 400

    return jsonify({"user_id": user.id, "otp_id": otp['response']}), 200
