"""Declarative base model for the SQLalchemy ORM"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all declarative objects"""
    pass
