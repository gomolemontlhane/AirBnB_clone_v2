#!/usr/bin/python3
"""Test module for the State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_instance(self):
        """Test instance creation"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test presence of attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_types(self):
        """Test attribute types"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_str(self):
        """Test __str__ method"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()

