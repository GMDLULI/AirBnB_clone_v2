#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from models.review import Review


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ 'places'

    if storage_type = 'db':
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        name = Column(String(128), nullable=False,)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        lattitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """ Returns a list of Review instances with place_id
            equals to current Place.id and FileStorage relationship
            between Place and Review
        """
        from models import storage

        lst = []
        revs = storage.all(Review)
        for i in revs.values():
            if i.place_id == self.id:
                lst.append(rev)
        return lst

    @property
    def amenities(self):
        """Returns the list of Amenity instances based on the
           attributes amenity_ids which contains all Amenity.id
           linked to the place
        """
        from models import storage

        lst = []
        revs = storage.all(Amenity)
        for am in revs.values():
            if am.id in self.amenity_ids:
                lst.append(am)
        return lst

    @amenities.setter
    def amenities(self, obj):
        """Adds Amenity.id to the attribute amenity_ids.
           accepts only Amenity objects
        """
        if obj is not None:
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
