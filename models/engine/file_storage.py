#!/usr/bin/python3
"""This Module fits for a File storage class"""
import os
import json
import datetime

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

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {i: j.to_dict() for i, j in FileStorage.__objects.items()}
            json.dump(dic, f)

    def new(self, val):
        """This puts in __objects the with appropraite key"""
        key = "{}.{}".format(type(val).__name__, val.id)
        FileStorage.__objects[key] = val

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
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            od = json.load(f)
            od = {i: self.classes()[j["__class__"]](**j)
                  for i, j in od.items()}
            FileStorage.__objects = od