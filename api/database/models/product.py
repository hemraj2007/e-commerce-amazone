from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    mrp = Column(Float, nullable=False)
    net_price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False, default=0)
    image = Column(String(255), nullable=True)  # Can store image URL or file path
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship with Category model
    category = relationship("Category", back_populates="products")
    # Relationship with Cart
    cart_items = relationship("Cart", back_populates="product", cascade="all, delete-orphan")
    # Relationship with Review
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
