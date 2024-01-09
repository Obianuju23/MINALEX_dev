#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, Enum, DateTime


class Task(BaseModel, Base):
    """User class"""
    __tablename__ = "task"
    user_id = Column(String(60), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    priority = Column(Enum("low", "medium", "high", "critical", "urgent", "on_hold", "normal", "none"), nullable=False, default="none")  # noqa E501
    status = Column(Enum("suspended", "abandoned", "completed", "in_progress", "ongoing", "review", "canceled", "deferred", "none"), nullable=False, default="none")  # noqa E501
    completed_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, nullable=True)
    assigned_to = Column(String(128), nullable=True)
    unassigned = Column(Enum("True", "False"), nullable=True, default="False")
    category = Column(Enum("Work", "Personal", "Home", "Meetings", "Health", "Errand", "Finances", "Social", "none"), nullable=True, default="none")  # noqa E501

    def __init__(self, user_id, name, description, priority, status, completed_date, due_date, assigned_to, unassigned, category):  # noqa E501
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.description = description
        self.priority = priority or "none"
        self.status = status or "none"
        self.completed_date = completed_date
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.unassigned = unassigned or "False"
        self.category = category or None
