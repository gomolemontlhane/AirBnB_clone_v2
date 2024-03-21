#!/usr/bin/python3
"""Test module for the City class"""
import unittest
import os
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        cls.city = City()
        cls.city.name = "Los Angeles"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Tear down test class"""
        del cls.city

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_conformance(self):
        """Test that models/city.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test presence of attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name', 'state_id']
        for attr in attributes:
            self.assertTrue(hasattr(self.city, attr))

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save(self):
        """Test save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['name'], "Los Angeles")
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['__class__'], "City")
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_str(self):
        """Test __str__ method"""
        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(string, str(self.city))

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()

