from dynaconf import FlaskDynaconf, settings
from flask import Flask

from {{cookiecutter.project_slug}} import views
from {{cookiecutter.project_slug}}.database import db, migrate


def create_app():
    app = Flask(__name__)

    FlaskDynaconf(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.get('sqlalchemy_database_uri')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.get('sqlalchemy_track_modifications', False)

    db.init_app(app)
    migrate.init_app(app, db)
    views.init_app(app)
    return app
