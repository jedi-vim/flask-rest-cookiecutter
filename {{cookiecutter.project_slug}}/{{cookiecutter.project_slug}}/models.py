from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from {{cookiecutter.project_slug}}.database import db


class Foo(db.Model):
    __tablename__ = 'foo'

    id = Column(Integer, primary_key=True)
    description = Column(String(30), nullable=False)
    foobar_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    foobar = relationship("Person")
