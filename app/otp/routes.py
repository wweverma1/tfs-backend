from flask import Blueprint

from app.otp.controller import (
    generate_otp,
    serve_otp,
    verify_otp,
)

otp_api = Blueprint('otp', __name__)

otp_api.add_url_rule(rule='/otp/<int:user_id>/generate',
                          view_func=generate_otp, methods=['GET', ])
otp_api.add_url_rule(rule='/otp/<int:otp_id>/serve',
                          view_func=serve_otp, methods=['GET', ])
otp_api.add_url_rule(rule='/otp<int:otp_id>/verify',
                          view_func=verify_otp, methods=['POST', ])
