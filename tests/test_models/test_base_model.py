#!/usr/bin/python3
"""BaseModel class unit test module"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """These are test cases for the BaseModel class"""
    def test_init(self):
        """Testing the initiation values"""
        model1 = BaseModel()

        self.assertIsNotNone(model1.id)
        self.assertIsNotNone(model1.created_at)
        self.assertIsNotNone(model1.updated_at)

    def test_to_dict(self):
        """This tests if a dict is copied"""
        
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        self.assertIsInstance(model1_dict, dict)
        self.assertEqual(model1_dict["__class__"], "BaseModel")
        self.assertEqual(model1_dict['id'], model1.id)
        self.assertEqual(model1_dict["created_at"], model1.created_at.isoformat())
        self.assertEqual(model1_dict["updated_at"], model1.updated_at.isoformat())

    def test_string(self):
        """This tests the printing of official string"""

        model1 = BaseModel()
        self.assertTrue(str(model1).startswith('[BaseModel]'))
        self.assertIn(model1.id, str(model1))
        self.assertIn(str(model1.__dict__), str(model1))

    def test_save(self):
        '''This tests the updated time'''
        model1 = BaseModel()
        first_update = model1.updated_at
        last_update = model1.save()

        self.assertNotEqual(first_update, last_update)

if __name__ == "__main__":
    unittest.main()