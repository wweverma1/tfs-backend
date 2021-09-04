from flask import Blueprint

from app.movies.controller import (
    movies,
)

movies_api = Blueprint('movies', __name__)

movies_api.add_url_rule(rule='/movies', view_func=movies, methods=['GET', ])
