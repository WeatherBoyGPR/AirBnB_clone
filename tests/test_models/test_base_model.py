#!/usr/bin/python3
"""Test ModulePackage:
    BaseModel Class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBase_Model(unittest.TestCase):
    """Test for BaseModel class methods
    """

    def test_instance(self):
        inst = BaseModel()

    def setUpClass(self):
        ''' Set two base models'''
        self.test0= BaseModel()
        self.base_model_ = BaseModel()

    def test_str(self):
        ''' Test __str__  '''
         self.assertIsInstance(self.test0.__str__(), str)

    def test_str_content(self):
        """checks content of __str__"""
        self.assertIn("[BaseModel]", self.B_base_model.__str__())

    def test_Init(self):
        ''' Checks if Init works'''
        self.assertIsInstance(self.A_base_model, BaseModel)
        self.assertIsInstance(self.B_base_model, BaseModel)

    def test_Id(self):
        ''' Test if each instance have an unique id '''
        self.assertNotEqual(self.A_base_model.id,
                            self.B_base_model.id)

    def test_id_str(self):
        '''test if id is str'''
        self.assertIsInstance(self.A_base_model.id, str)

    def test_date_is_date(self):
        '''test if dates are datetime type'''
        self.assertIsInstance(self.A_base_model.created_at, datetime)
        self.assertIsInstance(self.A_base_model.updated_at, datetime)

    def test_date_update(self):
        '''test if datetimes updates correctly'''
        self.A_base_model.save()
        self.assertNotEqual(self.A_base_model.created_at,
                            self.A_base_model.updated_at)

    def test_to_dict(self):
        """test if to_dict returns a dictionary"""
        self.assertIsInstance(self.A_base_model.to_dict(), dict)

    def test_to_dict_has_key(self):
        """test if to_dict works"""
        self.assertIn("created_at", self.A_base_model.to_dict())

    def test_add_attribute(self):
        """test adding attribute"""
        self.A_base_model.name = "pepe"
        self.assertEqual(self.A_base_model.name, "pepe")

    def test_kwarg(self):
        objdict = self.A_base_model.to_dict()
        self.kwarginstance = BaseModel(**objdict)
        self.assertIsInstance(self.kwarginstance, BaseModel)


if __name__ == "__main__":
    unittest.main()
