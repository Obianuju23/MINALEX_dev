#!/usr/bin/env python3
"""This the base template for all model object instances."""
from datetime import timedelta, datetime
from models.base import BaseModel, Base
from sqlalchemy import Column, String, Enum, DateTime
# import relationship
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    reset_token = Column(String(128), nullable=True)
    reset_token_expiry = Column(DateTime, nullable=True)
    reset_token_used = Column(Enum("True", "False", name="reset_token_used"), nullable=True, default="False", server_default="False")  # noqa E501
    role = Column(Enum("admin", "user", name="role_enum"), default="user", server_default="user")
    # set up a relationship with the task table
    task = relationship("Task", backref="user", cascade="all, delete, delete-orphan", passive_deletes=True)
    
    def __init__(self, email, first_name, last_name, password, role, middle_name=None, reset_token=None, reset_token_expiry=None, reset_token_used=None):  # noqa E501
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name or None
        self.email = email
        self.password = password
        self.role = role
        self.reset_token = reset_token
        self.reset_token_expiry = reset_token_expiry
        self.reset_token_used = reset_token_used

    # set token for the user
    def set_token(self, token):
        """Set the reset token for the user"""
        if token is None:
            return {"error": "token is required"}
        self.reset_token_expiry = datetime.now() + timedelta(minutes=10)
        self.reset_token_used = "False"
        self.reset_token = token
        self.save()
        return self
        
    # reset your password
    def reset_password(self, new_password, reset_token):
        """Reset the password for the user"""
        if new_password is None or reset_token is None:
            return {"error": "new_password and reset_token are required"}
        if self.reset_token_used == "True":
            return {"error": "reset token has already been used"}
        if self.reset_token_expiry < datetime.now():
            return {"error": "reset token has expired"}
        if self.reset_token != reset_token:
            return {"error": "invalid reset token"}
        self.password = new_password
        self.reset_token_used = "True"
        self.reset_token_expiry = None
        self.reset_token = None
        self.save()
        return self
    
    def update_password(self, new_password):
        """Update the password for the user"""
        if new_password is None:
            return {"error": "new_password is required"}
        self.password = new_password
        self.save()
        return self
