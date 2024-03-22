#!/usr/bin/python3
"""A module that creates the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """This Class manages Review objects"""

    place_id = ""
    user_id = ""
    text = ""