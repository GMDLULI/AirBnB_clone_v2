#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy Column, String
from models import Storage_type


class Amenity(BaseModel):
    """ Amenity class"""
    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)

    else:
        name = ""
