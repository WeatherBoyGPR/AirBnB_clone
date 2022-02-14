#!/usr/bin/python3
"""Test ModulePackage:
    Unittests for Review class below:
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """
        Test for Review class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = Review()
        self.assertIsInstance(Inst, Review)

    @classmethod
    def setUpClass(self):
        """ Test Review class """
        self.testReview = Review()

    def test_place_id(self):
        """ Test place_id attribute """
        self.testReview.place_id = ""
        self.assertIsInstance(self.testReview.place_id, str)

    def test_user_id(self):
        """ Test user_id attribute """
        self.testReview.user_id = ""
        self.assertIsInstance(self.testReview.user_id, str)

    def test_text(self):
        """ Test text attribute """
        self.testReview.text = "asfsafqf"
        self.assertIsInstance(self.testReview.text, str)

if __name__ == "__main__":
    unittest.main()
