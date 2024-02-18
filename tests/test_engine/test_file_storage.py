#!/usr/bin/python3s
import unittest
import pycodestyle
import os
import json
import inspect
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models.engine.file_storage

class TestSaveReloadBaseModel(unittest.TestCase):

    def test_default(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

    def test_reload_save_reload(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        print("-- Reloaded objects --")
        obj_id = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIsNotNone(all_objs[obj_id])

class TestFileStorageModel(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(FileStorage.__doc__, 'no docs for FileStorage Class')
        self.assertIsNotNone(models.engine.file_storage.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/engine/file_storage.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)
    
if __name__ == '__main__':
    unittest.main()
