#!/usr/bin/python3

"""
Defining BaseModel class that defines all common 
attributes/methods for other classes
"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class
    """

    def __init__(self):
        """
        Initialize for now
        """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        Print class name, id & dictionary
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 
        with current date & time
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        the instance
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
