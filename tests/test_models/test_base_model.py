#!/usr/bin/python3
"""Module for testing base_model.py"""
import json
import os
import pycodestyle
import unittest
import inspect
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test the BaseModel class"""

    def setUp(self):
        """Set up method"""
        self.base = BaseModel()

    def tearDown(self):
        """Tear down method"""
        del self.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_base_model(self):
        """Test pep8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Test docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods(self):
        """Test if methods exist"""
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.assertTrue(hasattr(BaseModel, 'to_dict'))

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save(self):
        """Test save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_init_BaseModel(self):
        """Test if the base is an instance of BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save_BaesModel(self):
        """Test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_uuid(self):
        """Test UUID"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2, instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Test __str__ method"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        del cls.base


class TestCodeFormat(unittest.TestCase):
    """Test code format"""
    def test_pycodestyle(self):
        """Test pep8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocstrings(unittest.TestCase):
    """Test docstrings"""
    def test_base_model_module_docstring(self):
        """Test base_model module docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_init_docstring(self):
        """Test __init__ method docstring"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_str_docstring(self):
        """Test __str__ method docstring"""
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_save_docstring(self):
        """Test save method docstring"""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_to_dict_docstring(self):
        """Test to_dict method docstring"""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()

