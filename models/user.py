#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """User class"""
    __tablename__ = "user"
    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    role = Column(String(128), nullable=False)
    #role = Column(Enum("admin", "user"), nullable=False, default="user")
    
    def __init__(self, email, first_name, last_name, middle_name, password, role):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name or None
        self.email = email
        self.password = password
        self.role = role or "user"
