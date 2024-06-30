#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declaritive import declarative_base
from models.base_model import BaseModel, Base

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    """ define tablename, specifying name of the table db """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
