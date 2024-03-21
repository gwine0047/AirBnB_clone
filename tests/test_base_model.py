#!/usr/bin/python3
"""BaseModel class unit test module"""

from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import uuid
import re
import json
import time
import unittest


class TestModel(unittest.TestCase):
    """These are test cases for the BaseModel class"""

    def PullOff(self):
        """Pulls down the methods for testing"""
        self.ResetStorage()
        pass

    def StartUp(self):
        """Starts up the methods for testing"""
        pass

    def ResetStorage(self):
        """Resets the Storage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_c_init_no_args(self):
        """Tests __init__ if it has no arguments."""
        self.ResetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_c_attributes(self):
        """Tests the value of attributes for BaseModel class instances"""

        ch = storage.attributes()["BaseModel"]
        model_I = BaseModel()
        for a, b in ch.items():
            self.assertTrue(hasattr(model_I, a))
            self.assertEqual(type(getattr(model_I, a, None)), b)
    
    def test_c_datetime_created(self):
        """This tests if created and updated time are same at when created"""

        current = datetime.now()
        model1 = BaseModel()
        current = model1.updated_at - model1.created_at
        time_diff = model1.created_at - current
        self.assertTrue(abs(time_diff.total_seconds()) < 0.1)

    def test_c_str(self):
        """Test for the official string method"""

        model1 = BaseModel()
        regex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        reset = regex.match(str(model1))
        self.assertIsNot(reset)
        self.assertEqual(reset.group(1), "BaseModel")
        self.assertEqual(reset.group(2), model1.id)
        str = reset.group(3)
        str = regex.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", str)
        dim = json.loads(str.replace("'", '"'))
        dim2 = model1.__dict__.copy()
        dim2["created_at"] = repr(dim2["created_at"])
        dim2["updated_at"] = repr(dim2["updated_at"])
        self.assertEqual(dim, dim2)

    def test_c_to_dict_args_none(self):
        """This tests the method to_dict() if no arguments"""

        self.ResetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.to_dict()
        txt = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), txt)

    def test_c_dict_many_args(self):
        """This tests to_dict() with excess arguments"""

        self.ResetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.to_dict(self, 98)
        txt = "to_dict() takes 1 positional arguments but 2 were given"
        self.assertEqual(str(err.exception), txt)

    def test_d_instancing(self):
        """This tests instancing with **kwargs"""

        model1 = BaseModel()
        model1.name = "Holberton"
        model1.my_number = 89
        model1_json = model1.to_dict()
        model_1 = BaseModel(**model1_json)
        self.assertEqual(model_1.to_dict(), model1.to_dict())

    def test_d_instancing_dict(self):
        """This tests instancing with **kwargs from a dictionary"""

        a = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at":datetime.now().isoformat(),
             "id":uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        model1 = BaseModel(**d)
        self.assertEqual(model1.to_dict(), a)

    def test_e_save(self):
        """This tests that from save(), storage.save() is called"""

        self.ResetStorage()
        model1 = BaseModel
        model1.save()
        key = "{}.{}".format(type(model1).__name__, model1.id)
        dic = {key: model1.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(dic)))
            f.seek(0)
            self.assertEqual(json.load(f), dic)

    def test_e_save_without_args(self):
        """This tests save()"""
        self.ResetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.save()
        txt = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), txt)

    def test_e_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.ResetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.save(self, 98)
        txt = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(err.exception), txt)

    def test_c_id(self):
        """This tests if user's id are unique"""

        mg = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(mg)), len(mg))

    def test_c_save(self):
        """This tests the save method - a public instance"""

        model1 = BaseModel()
        time.sleep(0.5)
        current = datetime.now()
        model1.save()
        diff = model1.updated_at - current
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_c_init_more_args(self):
        """Tests __init__ with plenty arguments"""
        self.ResetStorage()
        args = [a for a in range(1000)]
        model1 = BaseModel(0,1,2,3,4,5,6,7,8,9)
        model1 = BaseModel(*args)

    def test_c_instantiation(self):
        """This tests the instatiation of the BaseModel class"""

        model1 = BaseModel()
        self.assertEqual(str(type(model1)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(model1, BaseModel)
        self.assertTrue(issubclass(type(model1), BaseModel))


if __name__ == '__main__':
    unittest.main()