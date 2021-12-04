#!/usr/bin/python3
"""Test ModulePackage:
    User Class Unittests
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """
        Test for User class methods
    """

    def test_inst(self):
        inst = User()

    @classmethod
    def setUpClass(self):
        ''' Test Basic User'''
        self.user = User()
        self.user_model = User()

    def T_test_email(self):
        ''' Test email  '''
        user.email = "test@test.com"
        self.assertIsInstance(user.email, str)
        self.assertIsEqual(user.email, "test@test.com")

    def T_test_password(self):
        ''' Test password '''
        user.password = "Singapoore"
        self.assertIsInstance(user.password, str)
        self.assertIsEqual(user.password, "Singapoore")

    def T_first_name(self):
        ''' Test first_name '''
        user.first_name = "mike"
        self.assertIsInstance(user.first_name, str)
        self.assertIsEqual(user.first_name, "mike")

    def T_last_name(self):
        ''' Test last_name '''
        user.last_name = "hunt"
        self.assertIsInstance(user.last_name, str)
        self.assertIsEqual(user.last_name, "hunt")


if __name__ == "__main__":
    unittest.main()
