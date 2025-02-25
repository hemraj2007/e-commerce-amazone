from pydantic import BaseModel, conint
from datetime import datetime
from typing import Literal

class OrderCreate(BaseModel):
    user_id: int
    subtotal: float
    discount: float
    total: float
    status: Literal["pending", "shipped", "cancelled", "delivered"]
    shipping_address: str
    created_at: datetime
    updated_at: datetime

class OrderResponse(BaseModel):
    id: int
    user_id: int
    subtotal: float
    discount: float
    total: float
    status: Literal["pending", "shipped", "cancelled", "delivered"]
    shipping_address: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Ensures ORM compatibility
