#!/usr/bin/python3
""" """
import unittest
import pycodestyle
import uuid
import time
from datetime import datetime, timedelta
import inspect
import models.base_model
from models.base_model import BaseModel
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    
    def test_default(self):
        """ sample test case in the project"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                           my_model_json[key]))

    def test_initialization_id(self):
        """Test BaseModel id initialization"""
        new_model = BaseModel()
        self.assertIsInstance(new_model.id, str)
        try:
            self.assertIsInstance(uuid.UUID(new_model.id), uuid.UUID)
        except Exception as e:
            self.fail("id attribute is not a valid UUID")

    def test_initialization_dates(self):
        """Test BaseModel dates initialization"""
        new_model = BaseModel()
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertEqual(new_model.created_at, new_model.updated_at)
        self.assertAlmostEqual(new_model.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_str(self):
        """Test str format"""
        model = BaseModel()
        actual_format = str(model)
        expected_format = "[BaseModel] ({}) {}".format(model.id,
                                                       model.__dict__)
        self.assertEqual(actual_format, expected_format)

    def test_save(self):
        """Test save """
        new_model = BaseModel()
        old_update_at = new_model.updated_at
        old_created_at = new_model.created_at
        time.sleep(1)
        new_model.save()
        self.assertTrue((new_model.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_model.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        new_model = BaseModel()
        actual_dict = new_model.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "BaseModel")
        self.assertEqual(actual_dict["id"], new_model.id)
        self.assertEqual(datetime.fromisoformat(actual_dict["created_at"]), new_model.created_at)
        self.assertEqual(datetime.fromisoformat(actual_dict["updated_at"]), new_model.updated_at)

    def test_uniqueness(self):
        """Test unique id generation"""
        ids = set()
        for i in range(10):
            model = BaseModel()
            ids.add(model.id)
        self.assertEqual(len(ids), 10, "ids are not unique")

    def test_multiple_instances(self):
        """Test 2 instances creation with 2 different ids"""
        first_model = BaseModel()
        second_model = BaseModel()
        self.assertNotEqual(first_model.id, second_model.id)

    def test_multiple_save(self):
        """Test save behavior for 2 instances"""
        first_model = BaseModel()
        second_model = BaseModel()
        first_model.save()
        first_updated_at = first_model.updated_at
        second_model.save()
        second_updated_at = second_model.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(BaseModel.__doc__, 'no docs for BaseModel Class')
        self.assertIsNotNone(models.base_model.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    
    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/base_model.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
