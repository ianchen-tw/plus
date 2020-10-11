#! /bin/bash
# This file should be runned in container

pytest --pyargs /app -m smoke || (docker-compose --timestamps logs && exit 1)