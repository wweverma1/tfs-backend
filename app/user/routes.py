from flask import Blueprint

from app.user.controller import (
    create_user_account,
    user_login,
    verify_user_email,
    complete_user_profile,
    update_user_profile,
    update_user_password,
    fetch_user_profile,
    block_unblock_user,
    reset_user_password,
)

user_api = Blueprint('user', __name__)

user_api.add_url_rule(rule='/user/signup',
                      view_func=create_user_account, methods=['POST', ])
user_api.add_url_rule(rule='/user/login',
                      view_func=user_login, methods=['POST', ])
user_api.add_url_rule(rule='/user/<int:user_id>/verify',
                      view_func=verify_user_email, methods=['POST', ])
user_api.add_url_rule(rule='/user/<int:user_id>/completeprofile',
                      view_func=complete_user_profile, methods=['POST', ])
user_api.add_url_rule(rule='/user/<int:user_id>/updateprofile',
                      view_func=update_user_profile, methods=['POST', ])
user_api.add_url_rule(rule='/user/<int:user_id>/updatepswd',
                      view_func=update_user_password, methods=['POST', ])
user_api.add_url_rule(rule='/user/<int:user_id>/fetch', view_func=fetch_user_profile, methods=['GET', ])
user_api.add_url_rule(rule='/user/<int:user_id>/action', view_func=block_unblock_user, methods=['GET', ])
user_api.add_url_rule(rule='/user/resetpswd', view_func=reset_user_password, methods=['POST', ])
