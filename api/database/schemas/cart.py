from pydantic import BaseModel
from datetime import datetime

# User creation schema
class CartCreate(BaseModel):

    user_id : int
    product_id : int
    quantity : int
    created_at : datetime

# Response model (excluding sensitive data)
class CartResponse(BaseModel):

    id : int 
    user_id : int
    product_id : int
    quantity : int
    created_at : datetime

class CartUpdate(BaseModel):

    quantity : int

    class Config:
        from_attributes = True
