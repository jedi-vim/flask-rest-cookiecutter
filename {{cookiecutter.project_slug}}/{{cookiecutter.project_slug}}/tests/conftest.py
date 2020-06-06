import pytest

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.database import db


@pytest.fixture
def app(scope="session"):
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.drop_all(app=app)
        db.create_all(app=app)
        yield app.test_client()


# @pytest.fixture(autouse=True, scope="function")
def truncate(app):
    for table in db.metadata.sorted_tables:
        db.session.execute('TRUNCATE {} RESTART IDENTITY CASCADE'.format(table.name))
    db.session.commit()
