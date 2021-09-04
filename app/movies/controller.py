from datetime import datetime

from flask import (
    jsonify,
)


def movies():
    blockbuster = {
        "name": "Your Name",
        "desc": "Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.",
        "poster": "https://contentserver.com.au/assets/525768_gnau_yourname_p_v7_aa.jpg",
        "trailer": "https://www.youtube.com/watch?v=3KR8_igDs1Y",
        "duration": "1 Hour 52 Minutes",
        "lang": "English",
        "next_screening": datetime.now(),
    }
    other_movies = (
        {
            "name": "Your Name",
            "desc": "Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.",
            "poster": "https://contentserver.com.au/assets/525768_gnau_yourname_p_v7_aa.jpg",
            "trailer": "https://www.youtube.com/watch?v=3KR8_igDs1Y",
            "duration": "1 Hour 52 Minutes",
            "lang": "English",
            "next_screening": datetime.now(),
        },
        {
            "name": "Your Name",
            "desc": "Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.",
            "poster": "https://contentserver.com.au/assets/525768_gnau_yourname_p_v7_aa.jpg",
            "trailer": "https://www.youtube.com/watch?v=3KR8_igDs1Y",
            "duration": "1 Hour 52 Minutes",
            "lang": "English",
            "next_screening": datetime.now(),
        },
        {
            "name": "Your Name",
            "desc": "Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.",
            "poster": "https://contentserver.com.au/assets/525768_gnau_yourname_p_v7_aa.jpg",
            "trailer": "https://www.youtube.com/watch?v=3KR8_igDs1Y",
            "duration": "1 Hour 52 Minutes",
            "lang": "English",
            "next_screening": datetime.now(),
        },
        {
            "name": "Your Name",
            "desc": "Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.",
            "poster": "https://contentserver.com.au/assets/525768_gnau_yourname_p_v7_aa.jpg",
            "trailer": "https://www.youtube.com/watch?v=3KR8_igDs1Y",
            "duration": "1 Hour 52 Minutes",
            "lang": "English",
            "next_screening": datetime.now(),
        }
    )
    movies = {
        "blockbuster": blockbuster,
        "other_movies": other_movies
    }
    return jsonify(movies), 200
