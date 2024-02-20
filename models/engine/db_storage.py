#!/usr/bin/python3
"""_summary_
"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """_summary_
    """
    __engine = None
    __session = None

    def __init__(self):
        """_summary_
        """
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, id=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.
            id (_type_, optional): _description_. Defaults to None.
        """
        allClasses = [Amenity, City, State, User, Place, Review]
        result = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    className = obj.__class__.__name__
                    keyName = className + "." + str(obj.id)
                    result[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    className = obj.__class__.__name__
                    keyName = className + "." + str(obj.id)
                    result[keyName] = obj
        else:
            for clsss in allClasses:
                if id is not None:
                    obj = self.__session.query(clsss).get(id)
                    if obj is not None:
                        className = obj.__class__.__name__
                        keyName = className + "." + str(obj.id)
                        result[keyName] = obj
                else:
                    for obj in self.__session.query(clsss).all():
                        className = obj.__class__.__name__
                        keyName = className + "." + str(obj.id)
                        result[keyName] = obj
        return (result)

    def new(self, obj):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """_summary_
        """
        self.__session.commit()

    def delete(self, obj=None):
        """_summary_

        Args:
            obj (_type_, optional): _description_. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine,
                         expire_on_commit=False)
        )
        self.__session = Session()
