#! /usr/bin/env bash

# This is a prestart script hooked by tiangolo/uvicorn-gunicorn-fastapi:python3.7


# Let the DB start
python3 app/hooks/backend_prestart.py


# Run migrations
alembic upgrade head

# TODO: since we will drop and recreate all data after migration, it does not utilize migrations at all.
python3 app/hooks/initial_data.py
