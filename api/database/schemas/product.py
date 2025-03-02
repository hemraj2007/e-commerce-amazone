from pydantic import BaseModel
from datetime import datetime
from typing import Literal

# Product Create Schema
class ProductCreate(BaseModel):
    category_id: int
    name: str
    description: str
    mrp: float
    net_price: float
    quantity_in_stock: int
    image: str
    status: Literal["yes", "no"]  # Yes/No status
    created_at: datetime
    updated_at: datetime

# Product Response Schema
class ProductResponse(BaseModel):
    id: int
    category_id: int
    name: str
    description: str
    mrp: float
    net_price: float
    quantity_in_stock: int
    image: str
    status: Literal["yes", "no"]  # Yes/No status
    created_at: datetime
    updated_at: datetime

# Product Update Schema
class ProductUpdate(BaseModel):
    category_id: int
    name: str
    description: str
    mrp: float
    net_price: float
    quantity_in_stock: int
    image: str
    status: Literal["yes", "no"]  # Yes/No status
    updated_at: datetime

    class Config:
        from_attributes = True
