#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ amenity for a place """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
