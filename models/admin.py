from models.base import BaseModel, Base
from sqlalchemy import Column, String, Enum


class Admin(BaseModel, Base):
    """Admin class"""
    __tablename__ = "admin"
    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    role = Column(String(128), nullable=False)

    def __init__(self, email, first_name, last_name, password, role, middle_name=None):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name or None
        self.email = email
        self.password = password
        self.set_role(role)

    def set_role(self, role):
        """Set the role to 'admin'"""
        if role.lower() != "admin":
            raise ValueError("Invalid role. Only 'admin' is allowed.")
        self.role = "admin"
