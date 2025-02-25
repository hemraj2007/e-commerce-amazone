from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from api.database.connection import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mob_number = Column(String(15), unique=True, nullable=False)
    role = Column(Enum("customer", "admin", name="user_roles"), nullable=False, default="customer")
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship with Address model
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Cart
    cart_items = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Review
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Order
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
