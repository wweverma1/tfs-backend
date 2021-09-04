from app.utils.app_functions import (
    before_request,
    after_request,
)
from app.movies.routes import movies_api
from app.home.routes import home_api
from flask import Flask

app = Flask(__name__)


app.register_blueprint(home_api)
app.register_blueprint(movies_api)
