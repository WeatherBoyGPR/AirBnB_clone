#!/usr/bin/python3
"""Test ModulePackage:
    Unittests for classes below:
    User
    State
    City
    Amenity
    Place
    Review
"""

import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestBase_Model(unittest.TestCase):
    """
        Test for BaseModel class methods
    """

    def test_inst(self):
        inst = BaseModel()

    @classmethod
    def setUpClass(self):
        ''' Test Basic base models'''
        self.base = BaseModel()
        self.base_model = BaseModel()

    def test_str(self):
        ''' Test __str__  '''
        base = BaseModel()
        base_model = "[BaseModel]"
        self.assertIsInstance
        (self.base.__str__(), str)

    def test_str_content(self):
        """verify if __str__ content true"""
        self.assertIn("[BaseModel]", self.base_model.__str__())

    def test_Init(self):
        ''' Test Init'''
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base_model, BaseModel)

    def test_Id(self):
        ''' Test for unique id '''
        self.assertNotEqual(self.base.id, self.base_model.id)

    def test_id_str(self):
        '''test if id is an str'''
        self.assertIsInstance(self.base.id, str)

    def test_d_is_equal(self):
        '''test datetime'''
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

    def test_d_update(self):
        '''test if saved is equal'''
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

        def test_to_dict(self):
            """test if to_dict returns a dictionary"""
        self.assertIsInstance(self.base.to_dict(), dict)

    def test_to_dict_has_key(self):
        """test if to_dict works"""
        self.assertIn("created_at", self.base.to_dict())

    def test_add_attribute(self):
        """test adding attribute"""
        self.base.name = "name"
        self.assertEqual(self.base.name, "name")

    def test_kwarg(self):
        objdict = self.base.to_dict()
        self.kwarginstance = BaseModel(**objdict)
        self.assertIsInstance(self.kwarginstance, BaseModel)


class TestUser(unittest.TestCase):
    """
        Test for User class methods
    """

    def test_Init(self):
        """ Test Init """
        Inst = User()
        self.assertIsInstance(Inst, User)

    @classmethod
    def setUpClass(self):
        """ Test User class """
        self.testUser = User()

    def test_email(self):
        """ Test email attribute """
        self.testUser.email = "1234@goog.meep"
        self.assertIsInstance(self.testUser.email, str)

    def test_password(self):
        """ Test password attribute """
        self.testUser.password = "1234"
        self.assertIsInstance(self.testUser.password, str)

    def test_first_name(self):
        """ Test first_name attribute """
        self.testUser.first_name = "1234"
        self.assertIsInstance(self.testUser.first_name, str)

    def test_last_name(self):
        """ Test last_name attribute """
        self.testUser.last_name = "1234"
        self.assertIsInstance(self.testUser.last_name, str)

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
        self.testPlace.city_id =  ""
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

    def test_max_guests(self):
        """ Test max_guest attribute """
        self.testPlace.max_guest = 6
        self.assertIsInstance(self.testPlace.max_guest, int)

    def test_price_by_night(self):
        """ Test price_by_night attribute """
        self.testPlace.price_by_night = 45
        self.assertIsInstance(self.testPlace.price_by_night, int)

    def test_latitude(self):
        """ Test latitude attribute """
        self.testPlace.latitude = 42.35
        self.assertIsInstance(self.testPlace.latitude, float)

    def test_longitude(self):
        """ Test longitude attribute """
        self.testPlace.longitude = 42.41
        self.assertIsInstance(self.testPlace.longitude, float)

    def test_amenity_ids(self):
        """ Test amenity_ids attribute """
        self.testPlace.amenity_ids = []
        self.assertIsInstance(self.testPlace.amenity_ids, list)

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
