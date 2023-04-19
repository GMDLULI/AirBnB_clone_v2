#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models import storage_type
from sqlalchmey import Column, string
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(string(128), nullable=False)
        first_namei = Column(string(128), nullable=False)
        last_name = Column(string(128), nullable=False)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
