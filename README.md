# TFS backend

This is the back end of TFS, a project inspired by [BookMyShow](https://in.bookmyshow.com/). This project aims to aid a cinema theatre where visitors can view upcoming films and purchase tickets.


## Deployed on Heroku

[View Deployment](https://tfs-backend.herokuapp.com)

## Setup

- Install Python3.9.5
- Install requirements by running `pip install -r requirements.txt`

## Create Requirements file

- pip3 freeze > requirements.txt

## Start Virtual ENV

- source venv/bin/activate

## Start the server

- python app.py

## How to commit

Before committing any code, following codes must be run to ensure consistent formatting across branches, developer machines and successful tests -

- Auto formatting by running `autopep8 --in-place --recursive .`
- Check for remaining formatting issues by running `flake8 .` (To be fixed manually)
- Run unit tests to ensure that codebase functions as expected - `python -m pytest`
