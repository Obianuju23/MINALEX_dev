#!/usr/bin/env python3
"""module for the DBStorage class"""
import os
from dotenv import load_dotenv

from models.base import Base
from models.user import User
from models.task import Task
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()

clx = {"User": User, "Task": Task}


class DBStorage:
    """interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        # use the database URI from the environment variable
        minalex_db = os.getenv('DATABASE_URI')
        self.__engine = create_engine(minalex_db)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in clx:
            if cls is None or cls is clx[clss] or cls is clss:
                objs = self.__session.query(clx[clss]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        if self.__session:
            self.__session.remove()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session

    def get(self, cls, idx):
        """returns the object based on the class name and id"""
        if cls and idx:
            key_name = "{}.{}".format(cls.__name__, idx)
            return self.all(cls).get(key_name)
        return None

    def count(self, cls=None):
        """counts the number of objects in fle storage"""
        if cls:
            return len(self.all(cls))
        else:
            return len(self.all())
