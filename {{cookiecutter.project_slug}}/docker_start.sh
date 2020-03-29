#!/bin/sh
poetry run initialize_db
gunicorn -w 2 -b 0.0.0.0:4000 '{{cookiecutter.project_slug}}.app:create_app()'
