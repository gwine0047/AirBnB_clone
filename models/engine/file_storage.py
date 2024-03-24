#!/usr/bin/python3
"""This Module fits for a File storage class"""
import os
import json
import datetime
from models.base_model import BaseModel
from models.users import User

class FileStorage:
    """This helps class stores and retrieves data"""
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """A dictionary of valid classes is returned along"""
        from models.base_model import BaseModel
        from models.users import User
        from models.review import Review
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place

        all_class = {"BaseModel": BaseModel,
                     "User": User,
                     "State": State,
                     "Place": Place,
                     "City": City,
                     "Amenity": Amenity,
                     "Review": Review}
        return all_class
    
    def save(self):
        """This serializes objects to the Json file"""

        dict_obj = {}
        objs = FileStorage.__objects
        for obj in objs.keys():
            dict_obj[obj] = objs[obj].to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict_obj, f)

    def new(self, obj):
        """This puts in __objects the value with appropraite key"""

        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """This returns the dictionary __objects"""
        return FileStorage.__objects
    
    def attributes(self):
        """This shows the valid attributes and their types"""
        traits = {
            "BaseModel":
                {"id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name":str,
                 "last_name": str},
            "Place":
                {"name": str,
                 "city_id": str,
                 "user_id": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str},
            "Amenity":
                {"name": str},
            "City":
                {"name": str,
                 "state_id": str}
        }
        return traits
    
    def reload(self):
        """This reloads the stored objects"""
        if os.path.isfile(FileStorage.__file_path):        
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    od = json.load(f)
                    for key, val in od.items():
                        cls_name, obj_id = key.split('.')
                        cls = eval(cls_name)
                        inst_of_cls = cls(**val)
                        FileStorage.__objects[key] = inst_of_cls
                except Exception:
                    pass