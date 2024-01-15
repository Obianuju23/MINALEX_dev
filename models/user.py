#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import BaseModel, Base
from sqlalchemy import Column, String
# import relationship
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class"""
    __tablename__ = "user"
    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    role = Column(String(128), nullable=False)
    # set up a relationship with the task table
    task = relationship("Task", backref="user", cascade="all, delete, delete-orphan", passive_deletes=True)
    
    def __init__(self, email, first_name, last_name, password, role, middle_name=None):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name or None
        self.email = email
        self.password = password
        self.set_role(role)
        
    def set_role(self, role):
        """Set the role to 'user'"""
        if role.lower() != "user":
            raise ValueError("Invalid role. Only 'user' is allowed.")
        self.role = "user"
