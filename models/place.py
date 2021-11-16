#!/usr/bin/python3

from models.base_model import BaseModel

""" Holds Place class """


class Place(BaseModel):
    """ Place
        Represents place to be rented out
    Attributes:
    a. city_id (str) - City.id
    b. user_id (str) - User.id
    c. name (str) - name of place
    d. description (str) - description of place
    e. number_rooms (int) - number of rooms
    f. number_bathrooms (int) - number of bathrooms
    g. max_guest (int) - maximum number of guests
    h. price_by_night (int) - nightly rates
    i. latitude (float) - latitude of place
    j. longitude (float) - longitude of place
    k. amenity_ids (list of str) - Will serve as list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
