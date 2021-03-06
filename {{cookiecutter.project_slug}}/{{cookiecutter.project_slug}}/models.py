from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from {{ cookiecutter.project_slug }}.database import db


class User(db.Model):
    __tablename__ = '_user'

    id = Column(Integer, primary_key=True)
    login = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)


class Foo(db.Model):
    __tablename__ = 'foo'

    id = Column(Integer, primary_key=True)
    description = Column(String(30), nullable=False)
    foobar_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    foobar = relationship("Person")
