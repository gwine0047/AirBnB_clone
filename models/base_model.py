#!/usr/bin/python3
"""A python script which is the base model"""

import uuid
from datetime import datetime

class BaseModel:
    """This class will serve as a parent for other classes (others will inherit from it)"""

    def __init__(self, *args, **kwargs):
        """Initializing attributes"""

        t_f = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != None and kwargs != {}:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, t_f))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
    
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))