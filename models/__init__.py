#!/usr/bin/python3
"""This module instantiates an object of storage based on eviroment variable"""
from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()


"""Importing after storage to avoid circular imports"""

from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
