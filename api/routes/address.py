from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.address import AddressResponse, AddressCreate, AddressUpdate
from api.crud.address import create_address,delete_address,update_address,get_all_address
from typing import List

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=AddressResponse)
def add(address: AddressCreate , db:Session = Depends(get_db)):
    
    return create_address(db,address)


@router.get("/all_address", response_model=List[AddressResponse])
def list_category(db:Session = Depends(get_db)):
    return get_all_address(db)

@router.delete("/delete",response_model=dict)
def delete(address_id:int, db:Session = Depends(get_db)):
    return delete_address(db, address_id)

@router.put("/update", response_model=dict)
def update(address_id: int, address_data: AddressUpdate, db: Session = Depends(get_db)):
    return update_address(db, address_id, address_data)