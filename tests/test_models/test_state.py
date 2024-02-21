#!/usr/bin/python3
""" """
import os
import pycodestyle
from models.state import State
import inspect
import models.state
import time
from datetime import datetime, timedelta
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """
    def setUp(self):
        self.new_state = State()

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(State.__doc__, 'no docs for State Class')
        self.assertIsNotNone(models.state.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(State, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/state.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def test_init_state(self):
        self.assertIsInstance(self.new_state.created_at, datetime)
        self.assertIsInstance(self.new_state.updated_at, datetime)

    # def test_save_state(self):
    #     """Test save """
    #     new_state = State()
    #     old_update_at = new_state.updated_at
    #     old_created_at = new_state.created_at
    #     time.sleep(1)
    #     new_state.save()
    #     self.assertTrue((new_state.updated_at > old_update_at))
    #     self.assertTrue(old_created_at == new_state.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_state.name = "test_to_dict"
        actual_dict = self.new_state.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "State")
        self.assertEqual(actual_dict["id"], self.new_state.id)
        self.assertEqual(actual_dict["name"], self.new_state.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    
    def test_name3(self):
        """Tests the type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
