#!/usr/bin/python3
"""A python script which is the base model"""

import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """This class will serve as a parent for other classes (others will inherit from it)"""

    def __init__(self, *args, **kwargs):
        """Creating instance attributes

        Args:
            -args: is arguments list
            -**kwargs: is a dict of key-values arguments
        """

        if kwargs != None and kwargs != {}:
            for key in kwargs:
                if key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self):
        """This helps to return the official string representation"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the attribute self.update_at"""

        self.updated_at = datetime.now()
        # storage.save

    def to_dict(self):
        """turns __dict__ to a regular python dictionary"""

        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = type(self).__name__
        inst_dict["updated_at"] =  inst_dict["updated_at"].isoformat()
        inst_dict["created_at"] =  inst_dict["created_at"].isoformat()
        return inst_dict