#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models import storage_type
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ Amenity class"""
    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)

    else:
        name = ""
