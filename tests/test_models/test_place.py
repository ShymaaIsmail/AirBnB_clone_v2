#!/usr/bin/python3
""" """
import pycodestyle
from models.place import Place
import inspect
import models.place
import time
from datetime import datetime, timedelta
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """
    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(Place.__doc__, 'no docs for Place Class')
        self.assertIsNotNone(models.place.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(Place, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/place.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def test_init_place(self):
        self.assertIsInstance(self.new_place.created_at, datetime)
        self.assertIsInstance(self.new_place.updated_at, datetime)
        self.assertEqual(self.new_place.created_at, self.new_place.updated_at)
        self.assertAlmostEqual(self.new_place.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_save_place(self):
        """Test save """
        new_place = Place()
        old_update_at = new_place.updated_at
        old_created_at = new_place.created_at
        time.sleep(1)
        new_place.save()
        self.assertTrue((new_place.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_place.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_place.name = "test_to_dict"
        actual_dict = self.new_place.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "Place")
        self.assertEqual(actual_dict["id"], self.new_place.id)
        self.assertEqual(actual_dict["name"], self.new_place.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
