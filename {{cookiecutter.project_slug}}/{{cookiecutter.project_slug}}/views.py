from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from {{cookiecutter.project_slug}}.database import db
from {{cookiecutter.project_slug}}.models import Foo
from {{cookiecutter.project_slug}}.schemas import FooSchema

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


def init_app(app):
    app.register_blueprint(api_v1)


@api_v1.route('/')
def index():
    return 'It Works!'


@api_v1.route('/foo', methods=['POST'])
def create_foo():
    try:
        foo = FooSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    db.session.add(foo)
    db.session.commit()

    return FooSchema().dump(foo)
