from pydantic import BaseModel
from datetime import datetime

# User creation schema
class AddressCreate(BaseModel):

    user_id : int
    state : str 
    city : str 
    address_line1 : str 
    address_line2 : str 
    pincode : str 
    complete_address : str 
    created_at : datetime



# Response model (excluding sensitive data)
class AddressResponse(BaseModel):

    id : int 
    user_id : int
    state : str 
    city : str 
    address_line1 : str 
    address_line2 : str 
    pincode : str 
    complete_address : str 
    created_at : datetime
    
class AddressUpdate(BaseModel):
    
    state : str 
    city : str 
    address_line1 : str 
    address_line2 : str 
    pincode : str 
    complete_address : str 
    created_at : datetime


    class Config:
        from_attributes = True
