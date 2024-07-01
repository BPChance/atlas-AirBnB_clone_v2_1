#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, Foreignkey
from models.base_model import BaseModel, Base


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    place_id = Column(String(60), Foreignkey('places.id'), nullable=False)
    user_id = Column(String(60), Foreignkey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
