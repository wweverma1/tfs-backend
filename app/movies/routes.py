from flask import Blueprint

from app.movies.controller import (
    fetch_movies,
    fetch_movie,
    add_movie,
    edit_movie,
    delete_movie,
    add_screening,
    fetch_screening,
    delete_screening,
)

movies_api = Blueprint('movies', __name__)

movies_api.add_url_rule(rule='/movies/fetch',
                        view_func=fetch_movies, methods=['GET', ])
movies_api.add_url_rule(
    rule='/movies/<int:movie_id>/fetch', view_func=fetch_movie, methods=['GET', ])
movies_api.add_url_rule(
    rule='/movies/add', view_func=add_movie, methods=['POST', ])
movies_api.add_url_rule(rule='/movies/<int:movie_id>/edit',
                        view_func=edit_movie, methods=['PUT', ])
movies_api.add_url_rule(
    rule='/movies/<int:movie_id>/delete', view_func=delete_movie, methods=['GET', ])
movies_api.add_url_rule(rule='/movies/<int:movie_id>/screening/add',
                        view_func=add_screening, methods=['POST', ])
movies_api.add_url_rule(rule='/movies/<int:movie_id>/screening/<int:screening_id>/fetch',
                        view_func=fetch_screening, methods=['GET', ])
movies_api.add_url_rule(rule='/movies/<int:movie_id>/screening/<int:screening_id>/delete',
                        view_func=delete_screening, methods=['GET', ])
