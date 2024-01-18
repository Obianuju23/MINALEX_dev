# task.py

from models.base import BaseModel, Base
from sqlalchemy import Column, String, Enum, DateTime, ForeignKey


class Task(BaseModel, Base):
    """Task class"""
    __tablename__ = "tasks"
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False, unique=False)
    description = Column(String(512), nullable=False, unique=False)
    priority = Column(Enum("low", "medium", "high", "critical", "urgent", "on_hold", "normal", "none", name="priority_enum"), default="none", server_default="none")
    status = Column(Enum("suspended", "abandoned", "completed", "in_progress", "ongoing", "review", "canceled", "deferred", "none", name="status_enum"), default="none", server_default="none")
    completed_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, nullable=True)
    assigned_to = Column(String(128), nullable=True)
    unassigned = Column(Enum("True", "False", name="unassigned_enum"), nullable=True, default="False", server_default="False")
    category = Column(Enum("Work", "Personal", "Home", "Meetings", "Health", "Errand", "Finances", "Social", "none", name="category_enum"), nullable=True, default="none", server_default="none")

    def __init__(self, user_id, name, description, priority, status, completed_date, due_date, assigned_to, unassigned, category):
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
        self.category = category or "none"
