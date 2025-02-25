from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.review import ReviewResponse,ReviewCreate
from api.crud.review import create_review,get_all_review
from typing import List

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=ReviewResponse)
def add(review: ReviewCreate , db:Session = Depends(get_db)):
    
    return create_review(db,review)

@router.get("/all_products", response_model=List[ReviewResponse])
def list_products(db:Session = Depends(get_db)):
    return get_all_review(db)