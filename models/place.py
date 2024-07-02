#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

def get_place_amenity():
    from models import place_amenity
    return place_amenity



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary=get_place_amenity, viewonly=False, back_populates="place_amenities")

#   @property
#       def amenities(self):
#        """ returns list of amenity instances"""
#        from models import storage
#        from models.amenity import Amenity
#        amenity_list = []
#        for amenity_id in self.amenity_ids:
#            amenity = storage.get(Amenity, amenity_id)
#            if amenity:
#                amenity_list.append(amenity)
#        return amenity_list
#    
#    @amenities.setter
#    def amenities(self, amenity_obj):
#        """ handles append method for adding an Amenity.id """
#       from models.amenity import Amenity
#        if isinstance(amenity_obj, Amenity):
#            if amenity_obj.id not in self.amenity_ids:
#                self.amenity_ids.append(amenity_obj.id)
    

