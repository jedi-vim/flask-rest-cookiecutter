import click

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.database import db


@click.command(name='initialize_db')
def initialize_db():
    app = create_app()
    with app.app_context():
        db.create_all(app=app)
