from pydantic import BaseModel, Field
from datetime import datetime

# User creation schema
class ReviewCreate(BaseModel):

    user_id : int 
    order_id : int 
    product_id : int 
    rating: int = Field(..., ge=5, le=5) 
    review : str 
    created_at : datetime
# Response model (excluding sensitive data)
class ReviewResponse(BaseModel):

    id: int
    user_id : int 
    order_id : int 
    product_id : int 
    rating: int = Field(..., ge=5, le=5) 
    review : str 
    created_at : datetime

    class Config:
        from_attributes = True
