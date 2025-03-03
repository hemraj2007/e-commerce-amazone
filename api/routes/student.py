from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.student import StudentResponse, StudentCreate
from api.crud.student import create_student
from typing import List

# Creating an API router instance for handling student-related routes
router = APIRouter()

@router.post("/add", response_model=StudentResponse)
def add(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)
