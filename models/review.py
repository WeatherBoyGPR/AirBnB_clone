#!/usr/bin/python3

from models.base_model import BaseModel

""" Holds review class """


class Review(BaseModel):
    """ Review
        Stores text reviews
    Attributes:
    a. place_id (str) - Place.id
    b. user_id (str) - User.id
    c. text (str) - text contents of review
    """
    place_id = ""
    user_id = ""
    text = ""
