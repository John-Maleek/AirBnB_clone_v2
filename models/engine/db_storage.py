#!/usr/bin/python3
"""This model defines the DB storage class for AirBnB"""

from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        db_uri = 'mysql+mysqldb://{}:{}@{}3306/{}'.format(getenv(HBNB_MYSQL_USER), getenv(HBNB_MYSQL_PWD), getenv(HBNB_MYSQL_HOST), getenv(HBNB_MYSQL_DB))

        self.__engine = create_engine(db_uri, pool_pre_ping=True)
