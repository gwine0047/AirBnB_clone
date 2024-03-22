#!/usr/bin/python3
"""A module that creates the User class"""

from models.base_model import BaseModel

class City(BaseModel):
    """This Class manages City objects"""

    name = ""
    state_id = ""