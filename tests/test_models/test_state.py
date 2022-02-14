#!/usr/bin/python3
"""Test ModulePackage:
    Unittests for State class below:
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """
        Test for State class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = State()
        self.assertIsInstance(Inst, State)

    @classmethod
    def setUpClass(self):
        """ Test State class """
        self.testState = State()

    def test_name(self):
        """ Test name attribute """
        self.testState.name = "1234googmeep"
        self.assertIsInstance(self.testState.name, str)

if __name__ == "__main__":
    unittest.main()
