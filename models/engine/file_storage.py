#!/usr/bin/pytho3
"""
Defining FileStorage Class
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Class for Serializes and Deserializes
    Class Attributes:
    __file_path - string with JSON file path ('file.json')
    """
    __file_path = "file.json"
    """path to the JSON file"""
    __objects = {}
    """is a dictionary"""

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        """class name of an obj + id"""
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
            newdic_objs: store the keys and value that will save
                2. It passes trought for each key/val
                3. handels the files/ file handeling
                4. Then open the file path as a json file
                4.a. dumps the encoded data
                5. converts dic object into JSON strin data format
                5.a and writes 'w' to file 'json_f.write(dump(newdic obj))
        """
        newdict_objs = {}
        for key, val in self.__objects:
            newdict_objs[key] = val.to_dict()
        with open(self.__file_path, 'w') as json_f:
            json_f.write(json.dumps(newdict_objs))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as json_f:
                othrdict_objs = json.loads(json_f) #loads: decode json data
            for key, val in othrdict_objs.items():
                self.__objects[key] = BaseModel(**val)
