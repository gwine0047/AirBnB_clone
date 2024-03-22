#!/usr/bin/python3
"""A module that creates the Place class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """This Class manages Place objects"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    price_by_night = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    logitude = 0.0
    amenity_ids = []