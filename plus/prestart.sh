#! /usr/bin/env bash

## remove database file
echo remove database
rm -rf /app/sql_app.db

# This is a prestart script hooked by tiangolo/uvicorn-gunicorn-fastapi:python3.7


# Let the DB start
python3 app/hooks/backend_prestart.py


# TODO: run migrations


# TODO: create initialdata into DB

python3 app/hooks/initial_data.py
