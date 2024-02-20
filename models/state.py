#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)

        cities = relationship('City', cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """Getters"""
            from models import storage
            citiesLst = []
            allCities = storage.all(City)
            for city in allCities.values():
                if city.state_id == self.id:
                    citiesLst.append(city)
            return (citiesLst)
