from datetime import datetime

# Standard library imports
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

from app.movies.models import(
    Movie,
)

from app.movies.validators import(
    CreateMovieSchema,
)


def add_movie():
    err = CreateMovieSchema().validate(request.form)
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    name = request.form['name']
    lang = request.form['lang']
    description = request.form['description']
    duration = request.form['duration']
    is_blockbuster = True if request.form['is_blockbuster'] == "True" else False
    poster_url = request.form['poster_url'] if 'poster_url' in request.form else None
    trailer_url = request.form['trailer_url'] if 'trailer_url' in request.form else None

    movie = Movie.create(name, lang, description, duration,
                         is_blockbuster, poster_url, trailer_url)
    if not movie:
        return "Error creating Movie", 400
    return jsonify({"id": movie.id}), 200


def fetch_movies():
    movies = {}
    blockbuster = []
    other_movies = []
    movies_list = db.session.query(Movie.id, Movie.name, Movie.description, Movie.poster_url, Movie.trailer_url,
                                   Movie.lang, Movie.duration, Movie.is_blockbuster).filter(Movie.last_screening > datetime.now()).all()
    for movie in movies_list:
        movie_data = {
            "id": movie.id,
            "name": movie.name,
            "desc": movie.description,
            "poster": movie.poster_url,
            "trailer": movie.trailer_url,
            "duration": movie.duration,
            "lang": movie.lang
            # "next_screening": movie.next_screening(),
        }
        if movie.is_blockbuster == True:
            blockbuster.append(movie_data)
        else:
            other_movies.append(movie_data)
    movies["blockbuster"] = blockbuster
    movies["other_movies"] = other_movies
    return jsonify(movies), 200


def fetch_movie(movie_id):
    movie = db.session.query(Movie.id, Movie.name, Movie.description, Movie.poster_url, Movie.trailer_url,
                             Movie.lang, Movie.duration).filter(Movie.id == movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to Fetch Movie", 400
    movie_data = {
        "id": movie.id,
        "name": movie.name,
        "desc": movie.description,
        "poster": movie.poster_url,
        "trailer": movie.trailer_url,
        "duration": movie.duration,
        "lang": movie.lang
    }
    # add screenings to movie_data
    return jsonify(movie_data), 200


def edit_movie(movie_id):
    movie = db.session.query(Movie).filter(Movie.id == movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to Update Movie details", 400
    try:
        if 'name' in request.form:
            movie.name = request.form['name']
        if 'lang' in request.form:
            movie.lang = request.form['lang']
        if 'description' in request.form:
            movie.description = request.form['description']
        if 'duration' in request.form:
            movie.duration = request.form['duration']
        if 'is_blockbuster' in request.form:
            movie.is_blockbuster = True if request.form['is_blockbuster'] == "True" else False
        if 'poster_url' in request.form:
            movie.poster_url = request.form['poster_url']
        if 'trailer_url' in request.form:
            movie.poster_url = request.form['poster_url']
        db.session.commit()
        return "Movie Edited", 200
    except:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Update Movie Details", 400


def delete_movie(movie_id):
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to delete", 400
    # code to delete the movie, its screenings and its seats
    try:
        db.session.delete(movie)
        db.session.commit()
        return "Movie Deleted", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Delete Movie", 400


def add_screening():
    return "Screening Added", 200


def fetch_screenings():
    return "Screenings Fetched", 200


def delete_screening():
    return "Screening Deleted", 200
