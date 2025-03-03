from sqlalchemy import Column, Integer, String
from api.database.connection import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    address = Column(String(255), nullable=False)  # Address should be String
    subject = Column(String(100), nullable=False)  # Subject should be String
