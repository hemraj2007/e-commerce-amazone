from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

# Define Enum for Role
class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

# User creation schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: UserRole
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

# Response model (excluding sensitive data)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    mob_number: str

    class Config:
        from_attributes = True

# ✅ Corrected: Password update schema (should be separate)
class UserPasswordUpdate(BaseModel):
    new_password: str
    confirm_password: str

    class Config:
        from_attributes = True

# User login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str   
