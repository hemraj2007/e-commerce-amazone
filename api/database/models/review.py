from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, CheckConstraint
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    rating = Column(Integer, nullable=False)  # Ensure values are between 1-5
    review = Column(String(500), nullable=True)  # Review text (optional)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # SQLAlchemy Check Constraint to enforce rating between 1-5
    __table_args__ = (CheckConstraint("rating BETWEEN 1 AND 5", name="check_rating_range"),)


    # Relationships
    user = relationship("User", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")
