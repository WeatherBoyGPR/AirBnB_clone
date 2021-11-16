#!/usr/bin/python3

from models.base_model import BaseModel

""" Holds City class """


class City(BaseModel):
    """ City
        Represents a city
    Attributes:
    a. state_id (str) - id of State
    b. name (str) - name of City
    """
    state_id = ""
    name = ""
