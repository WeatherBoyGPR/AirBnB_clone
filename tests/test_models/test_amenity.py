#!/usr/bin/python3
"""Test ModulePackage:
    Unittests for Amenity class below:
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
        Test for Amenity class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = Amenity()
        self.assertIsInstance(Inst, Amenity)

    @classmethod
    def setUpClass(self):
        """ Test Amenity class """
        self.testAmenity = Amenity()

    def test_Amenity(self):
        """ Test name attribute """
        self.testAmenity.name = "1234googmeep"
        self.assertIsInstance(self.testAmenity.name, str)

if __name__ == "__main__":
    unittest.main()
