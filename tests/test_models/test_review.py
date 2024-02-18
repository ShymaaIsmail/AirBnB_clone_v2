#!/usr/bin/python3
""" """
import pycodestyle
from models.state import State
import inspect
import models.state
import time
from datetime import datetime, timedelta
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """
    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(Review.__doc__, 'no docs for Review Class')
        self.assertIsNotNone(models.review.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(Review, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/review.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def test_init_review(self):
        self.assertIsInstance(self.new_review.created_at, datetime)
        self.assertIsInstance(self.new_review.updated_at, datetime)
        self.assertEqual(self.new_review.created_at, self.new_review.updated_at)
        self.assertAlmostEqual(self.new_review.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_save_review(self):
        """Test save """
        new_review = Review()
        old_update_at = new_review.updated_at
        old_created_at = new_review.created_at
        time.sleep(1)
        new_review.save()
        self.assertTrue((new_review.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_review.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_review.text = "test_to_dict"
        actual_dict = self.new_review.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "Review")
        self.assertEqual(actual_dict["id"], self.new_review.id)
        self.assertEqual(actual_dict["text"], self.new_review.text)
        self.assertEqual(actual_dict["text"], "test_to_dict")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
