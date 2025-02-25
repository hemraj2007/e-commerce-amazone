from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255), nullable=True)
    pincode = Column(String(10), nullable=False)
    complete_address = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relationship with User model
    user = relationship("User", back_populates="addresses")
