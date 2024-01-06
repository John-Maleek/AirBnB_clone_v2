#!/usr/bin/python3
"""This model defines the DB storage class for AirBnB"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

all_classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """...
        Attributes:
        __engine: The SQLAlchemy engine
        __session: The SQLAlchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        for entry in all_classes:
            if cls is None or cls is all_classes[entry] or cls is entry:
                all_obj = self.__session.query(all_classes[entry]).all()
                for obj in all_obj:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def update(self, cls, obj_id, key, new_value):
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

    def delete(self, obj=None):
        if obj is None:
            return
        self.__session.delete(obj)

    def close(self):
        self.__session.remove()
