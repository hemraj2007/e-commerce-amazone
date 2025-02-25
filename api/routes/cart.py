from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.cart import CartResponse, CartCreate, CartUpdate
from api.crud.cart import create_cart,delete_cart, update_cart,get_all_cart
from typing import List

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=CartResponse)
def add(cart: CartCreate , db:Session = Depends(get_db)):
    
    return create_cart(db,cart)

@router.get("/all_category", response_model=List[CartResponse])
def list_category(db:Session = Depends(get_db)):
    return get_all_cart(db)

@router.delete("/delete",response_model=dict)
def delete(cart_id:int, db:Session = Depends(get_db)):
    return delete_cart(db, cart_id)


@router.put("/update", response_model=dict)
def update(cart_id: int, cart_data: CartUpdate, db: Session = Depends(get_db)):
    return update_cart(db, cart_id, cart_data)