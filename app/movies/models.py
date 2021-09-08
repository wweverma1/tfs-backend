# Standard library imports
from datetime import datetime
import traceback

# Related third party imports
from sqlalchemy.exc import SQLAlchemyError

# Local app specific imports
from app import (
    db,
    SCHEMA_NAME,
)


class Movie(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    name = db.Column(db.String(100))
    lang = db.Column(db.String(10))
    description = db.Column(db.Text)
    poster_url = db.Column(db.Text, nullable=True, default=None)
    trailer_url = db.Column(db.Text, nullable=True, default=None)
    duration = db.Column(db.Integer)
    is_blockbuster = db.Column(db.Boolean)
    first_screening = db.Column(db.DateTime)
    last_screening = db.Column(db.DateTime)

    @staticmethod
    def create(name=None, lang=None, description=None, duration=None, is_blockbuster=None, poster_url=None, trailer_url=None):
        try:
            movie = Movie(
                created_at=datetime.now(),
                name=name,
                lang=lang,
                description=description,
                poster_url=poster_url,
                trailer_url=trailer_url,
                duration=duration,
                is_blockbuster=is_blockbuster
            )
            db.session.add(movie)
            db.session.commit()
            return movie
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
