from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    address: str
    subject: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    subject: Optional[str] = None

class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True
