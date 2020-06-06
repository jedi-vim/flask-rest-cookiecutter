import factory
from factory.alchemy import SQLAlchemyModelFactory
from {{cookiecutter.project_slug}}.database import db
from {{cookiecutter.project_slug}}.models import Foo


class FooFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Foo
        sqlalchemy_session = db.session

    description = factory.Sequence(lambda n: 'foo {0}'.format(n))
