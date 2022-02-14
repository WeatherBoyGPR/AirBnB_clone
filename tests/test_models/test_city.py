#!/usr/bin/python3
"""Test ModulePackage:
    Unittests for City class below:
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """
        Test for City class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = City()
        self.assertIsInstance(Inst, City)

    @classmethod
    def setUpClass(self):
        """ Test City class """
        self.testCity = City()

    def test_state_id(self):
        """ Test state_id attribute """
        self.testCity.state_id = 1423
        self.assertIsInstance(self.testCity.state_id, int)

    def test_name(self):
        """ Test name attribute """
        self.testCity.name = "Jefferson"
        self.assertIsInstance(self.testCity.name, str)

if __name__ == "__main__":
    unittest.main()
