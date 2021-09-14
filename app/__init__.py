# Standard library imports
import os

# Related third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Local app specific imports
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 50
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
SCHEMA_NAME = os.getenv("SCHEMA_NAME")

from app.movies.routes import movies_api
from app.home.routes import home_api
from app.bookings.routes import bookings_api
# from app.otp.routes import otp_api
# from app.seats.routes import seats_api
# from app.user.routes import user_api

app.register_blueprint(bookings_api)
app.register_blueprint(home_api)
app.register_blueprint(movies_api)

from app.utils.app_functions import (
    before_request,
    after_request,
)
