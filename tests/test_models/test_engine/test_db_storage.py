#!/usr/bin/python3s
import unittest
import pycodestyle
import os
import json
import inspect
from models import storage
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import models.engine.db_storage

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', "DB storage not enabled")
class TestSaveReloadBaseModel(unittest.TestCase):
    pass


@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', "DB storage not enabled")
class TestDBStorageModel(unittest.TestCase):

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(DBStorage.__doc__, 'no docs for DBStorage Class')
        self.assertIsNotNone(models.engine.db_storage.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/engine/db_storage.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)
    
if __name__ == '__main__':
    unittest.main()
