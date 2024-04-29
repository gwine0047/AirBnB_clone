#!/usr/bin/python3
"""
A Base class Model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
     defines all common attributes/methods for other classes
     """
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        # making a copy of the dict rep of obj
        instance_dict = self.__dict__.copy()
        # a key __class__ must be added to this dictionary 
        # with the class name of the object
        instance_dict["__class__"] = self.__class__.__name__

        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        string representation of an object
        """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')