#!/usr/bin/python3
"""Test module for the Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance(self):
        """Test instance creation"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test presence of attributes"""
        review = Review()
        attributes = ['place_id', 'user_id', 'text']
        for attr in attributes:
            self.assertTrue(hasattr(review, attr))

    def test_attribute_types(self):
        """Test attribute types"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_str(self):
        """Test __str__ method"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()

