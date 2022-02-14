#!/usr/bin/python3
""" Unittest for class Place """

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """
        Test for Place class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = Place()
        self.assertIsInstance(Inst, Place)

    @classmethod
    def setUpClass(self):
        """ Test Place class """
        self.testPlace = Place()

    def test_city_id(self):
        """ Test city_id attribute """
        self.testPlace.city_id = ""
        self.assertIsInstance(self.testPlace.city_id, str)

    def test_user_id(self):
        """ Test user_id attribute """
        self.testPlace.user_id = ""
        self.assertIsInstance(self.testPlace.user_id, str)

    def test_name(self):
        """ Test name attribute """
        self.testPlace.name = "nantucket"
        self.assertIsInstance(self.testPlace.name, str)

    def test_description(self):
        """ Test description attribute """
        self.testPlace.description = "hold"
        self.assertIsInstance(self.testPlace.description, str)

    def test_number_rooms(self):
        """ Test number_rooms attribute """
        self.testPlace.number_rooms = 4
        self.assertIsInstance(self.testPlace.number_rooms, int)

    def test_number_bathrooms(self):
        """ Test number_bathorooms attribute """
        self.testPlace.number_bathrooms = 4
        self.assertIsInstance(self.testPlace.number_bathrooms, int)

if __name__ == "__main__":
    unittest.main()
