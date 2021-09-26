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

from app.movies.models import (
    Movie,
    Screening,
)

from app.movies.validators import (
    CreateMovieSchema,
    CreateScreeningSchema,
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
                                   Movie.lang, Movie.duration, Movie.is_blockbuster)\
        .filter(Movie.last_screening_timing > datetime.now()).all()
    for movie in movies_list:
        next_screening = db.session.query(Screening.timing).filter(
            Screening.movie_id == movie.id, Screening.timing > datetime.now()).order_by(Screening.timing).first()
        movie_data = {
            "id": movie.id,
            "name": movie.name,
            "desc": movie.description,
            "poster": movie.poster_url,
            "trailer": movie.trailer_url,
            "duration": movie.duration,
            "lang": movie.lang,
            "next_screening": next_screening.timing if next_screening else None,
        }
        if movie.is_blockbuster is True:
            blockbuster.append(movie_data)
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
        "lang": movie.lang,
    }
    screenings_list = db.session.query(Screening).filter(
        Screening.movie_id == movie_id, Screening.timing > datetime.now()).all()
    screenings = []
    for screening in screenings_list:
        screening_data = {
            "id": screening.id,
            "timing": screening.timing,
        }
        screenings.append(screening_data)
    movie_data["screenings"] = screenings
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
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Update Movie Details", 400


def delete_movie(movie_id):
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to delete", 400
    # delete the movie, its screenings and its seat arrangement
    try:
        db.session.query(Screening).filter(
            Screening.movie_id == movie.id).delete()
        db.session.delete(movie)
        db.session.commit()
        return "Movie Deleted", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Delete Movie", 400


def add_screening(movie_id):
    err = CreateScreeningSchema().validate(request.form)
    if len(err) != 0:
        print(err)
        return json.dumps(err), 400

    timing = request.form['timing']

    # if timing < datetime.now():
    #     return "Screening time should be after current time", 400

    movie = db.session.query(Movie).filter(Movie.id == movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to add Screening", 400
    screening = Screening.create(movie_id, timing)
    if not screening:
        return "Error creating Screening", 400
    try:
        if (movie.last_screening_timing is None or screening.timing > movie.last_screening_timing):
            movie.last_screening_id = screening.id
            movie.last_screening_timing = screening.timing
        db.session.commit()
        return jsonify({"id": screening.id}), 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't Update Movie Details", 400


def fetch_screening(movie_id, screening_id):
    movie = db.session.query(Movie.id).filter(
        Movie.id == movie_id).one_or_none()
    if not movie:
        return "Invalid Movie ID, Unable to add Screening", 400
    screening = db.session.query(Screening).filter(
        Screening.movie_id == movie.id, Screening.id == screening_id).one_or_none()
    screening_data = {
        "id": screening.id,
        "timing": screening.timing
    }
    return screening_data, 200


def delete_screening(movie_id, screening_id):
    screening = Screening.query.filter_by(id=screening_id).one_or_none()
    if not screening:
        return "Invalid Screening ID, Unable to delete", 400
    try:
        movie = db.session.query(Movie).filter(
            Movie.id == movie_id).one_or_none()
        screenings = db.session.query(Screening).filter(
            Screening.movie_id == movie.id).order_by(Screening.timing).all()
        if movie.last_screening_id == screening.id:
            if len(screenings) == 1:
                movie.last_screening_id = None
                movie.last_screening_timing = None
            else:
                movie.last_screening_id = screenings[-2].id
                movie.last_screening_timing = screenings[-2].timing
        db.session.delete(screening)
        db.session.commit()
        return "Screening Deleted", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Couldn't delete Screening", 400
