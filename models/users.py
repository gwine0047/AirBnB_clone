#!/usr/bin/python3
"""A module that creates the User class"""

from models.base_model import BaseModel

class User(BaseModel):
    """This Class manages User objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""