def generate_otp(user_id):
    return "OTP", 200


def serve_otp(otp_id):
    return "OTP SENT", 200


def verify_otp():
    return "Success", 200
