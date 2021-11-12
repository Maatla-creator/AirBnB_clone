#!/usr/bin/python3

"""
Module test_base_model
Contains the test cases for module base_model
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """
    Testing instantiation
    """
    def test_init_type(self):
        """
        Tests initialization of base_model attributes
        """
        my_model = BaseModel()
        my_model.name = "my_name"
        my_model.my_number = 89
        self.assertTrue(type(my_model), BaseModel)
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertTrue(my_model.name, "my_name")

if __name__ == '__main__':
    unittest.main()
