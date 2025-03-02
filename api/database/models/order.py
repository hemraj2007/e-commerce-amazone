from sqlalchemy import Column, Integer, ForeignKey, String, Enum, Float, DateTime, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subtotal = Column(Float, nullable=False)
    discount = Column(Float, default=0.0, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(Enum("pending", "shipped", "cancelled", "delivered", name="order_status"), default="pending", nullable=False)
    shipping_address = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)



    # Relationships
    user = relationship("User", back_populates="orders")
    # Relationship with Review
    reviews = relationship("Review", back_populates="order", cascade="all, delete-orphan")
    