#!/usr/bin/python3
"""Test module for the Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instance(self):
        """Test instance creation"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test presence of attributes"""
        place = Place()
        attributes = ['city_id', 'user_id', 'name', 'description',
                      'number_rooms', 'number_bathrooms', 'max_guest',
                      'price_by_night', 'latitude', 'longitude',
                      'amenity_ids']
        for attr in attributes:
            self.assertTrue(hasattr(place, attr))

    def test_attribute_types(self):
        """Test attribute types"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_str(self):
        """Test __str__ method"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test_is_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()

