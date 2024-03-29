from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """Base class for gadgets. This class does not map to a table."""

    id = Column(String(60), nullable=False, primary_key=True, default=str(uuid.uuid4))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                setattr(self, k, v)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """String representation of the class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def to_dict(self):
        """Dictionary representation of the class"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        if "password" in obj_dict:
            del obj_dict["password"]
            # Exclude 'users' attribute
        if "users" in obj_dict:
            del obj_dict["users"]
        if "admin" in obj_dict:
            del obj_dict["admin"]
        return obj_dict

    def save(self):
        """Save object instance to the database"""
        from models import storage
    
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
    
        storage.delete(self)
        storage.save()
