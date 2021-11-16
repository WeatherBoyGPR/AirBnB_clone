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

    def test_inst(self):
        inst = BaseModel()

    def setUpClass(self):
        ''' Test Basic base models'''
        self.base = BaseModel()
        self.base_model_ = BaseModel()

    def test_str(self):
        ''' Test __str__  '''
        base = BaseModel()
        base_model = "[BaseModel]"
        self.assertIsInstance(self.base.id, self.test0.__str__(), str)

    def test_str_content(self):
        """verify if __str__ content true"""
        self.assertIn("[BaseModel]", self.base_model.__str__())

    def test_Init(self):
        ''' Test Init'''
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base_model, BaseModel)

    def test_Id(self):
        ''' Test for unique id '''
        self.assertNotEqual(self.base.id,
                            self.base_model.id)

    def test_id_str(self):
        '''test if id is an str'''
        self.assertIsInstance(self.base.id, str)

    def test_d_is_equal(self):
        '''test datetime'''
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_d_update(self):
        '''test if saved is equal'''
        self.base.save()
        self.assertNotEqual(self.base.created_at,
                            self.base.updated_at)

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


if __name__ == "__main__":
    unittest.main()
