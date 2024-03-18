#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """ Database storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(os.getenv('HBNB_MYSQL_USER'),
                                               os.getenv('HBNB_MYSQL_PWD'),
                                               os.getenv('HBNB_MYSQL_HOST'),
                                               os.getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query objects """
        objs = {}
        all_classes = (User, Place, State, City, Amenity, Review)
        if cls:
            if cls in all_classes:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        else:
            for class_typ in all_classes:
                objects = self.__session.query(class_typ).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
