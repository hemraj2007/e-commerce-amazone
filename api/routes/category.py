from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.category import CategoryResponse, CategoryCreate
from api.crud.category import create_category,delete_category,get_all_category
from typing import List

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=CategoryResponse)
def add(category: CategoryCreate , db:Session = Depends(get_db)):
    
    return create_category(db,category)

@router.get("/all_category", response_model=List[CategoryResponse])
def list_category(db:Session = Depends(get_db)):
    return get_all_category(db)


@router.delete("/delete",response_model=dict)
def delete(category_id:int, db:Session = Depends(get_db)):
    return delete_category(db, category_id)
