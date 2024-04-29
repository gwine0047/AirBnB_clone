#!/usr/bin/python3
"""
test model for the Base class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testing methods"""
    def test_init(self):
        """ Testing the initialization"""
        test_model = BaseModel()

        # testing if each feature exist
        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)

    def test_save(self):
        """test for the save method"""
        test_model = BaseModel()
        # asserting that the past and present updated at are not equal
        past = test_model.updated_at
        present = test_model.save()

        self.assertNotEqual(past, present)

    def test_to_dict(self):
        """testing the serialization"""
        test_model = BaseModel()

        # serialization (changing the obj to a dict)
        test_model_dict = test_model.to_dict()
        self.assertIsInstance(test_model_dict, dict)

        self.assertEqual(test_model_dict["__class__"], 'BaseModel')
        self.assertEqual(test_model_dict['id'], test_model.id)
        self.assertEqual(test_model_dict['created_at'], test_model.created_at.isoformat())
        self.assertEqual(test_model_dict['updated_at'], test_model.updated_at.isoformat())

    def test_str(self):
        """
        testing the string representation
        of the BaseModel class
        """
        test_model = BaseModel()

        self.assertTrue(str(test_model).startswith('[BaseModel]'))
        # assert that id is in the string representation test_model
        self.assertIn(test_model.id, str(test_model))
        # asssert that the dict rep (which is a string) in the __str__ method
        self.assertIn(str(test_model.__dict__), str(test_model))

if __name__ == "__main__":
    unittest.main()