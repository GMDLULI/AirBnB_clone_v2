#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """place tests class"""

    def __init__(self, *args, **kwargs):
        """init test class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """testing place city_id attr """
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ testing place user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """testing place name attr """
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """testing place description attr """
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """testing place number of rooms attr """
        new = self.value()
        self.assertEqual(type(new.user_id), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """testing place number of bathrooms attr """
        new = self.value()
        self.assertEqual(type(new.user_id), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """testing place max guest attr """
        new = self.value()
        self.assertEqual(type(new.user_id), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """testing place price by night attr """
        new = self.value()
        self.assertEqual(type(new.user_id), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """testing place latitude attr """
        new = self.value()
        self.assertEqual(type(new.user_id), in if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """ testing place logitude attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """testing place amenity_id attr """
        new = self.value()
        self.assertEqual(type(new.user_id), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
