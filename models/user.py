#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """User class"""
    __tablename__ = "user"

    def __init__(self):
        super().__init__(*args, **kwargs)