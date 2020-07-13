#! /bin/sh
# This file should be runned in container

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports /app

# remove unused imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place /app --exclude=__init__.py

# sort and gather imports
isort /app

# formatter
black /app
