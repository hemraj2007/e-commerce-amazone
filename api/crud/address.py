from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.address import Address
from api.database.schemas.address import AddressCreate,AddressUpdate

def create_address(db: Session,  address: AddressCreate):
    
    db_address = Address(
        user_id = address.user_id,
        state = address.state,
        city = address.city,
        address_line1 = address.address_line1,
        address_line2 = address.address_line2,
        pincode = address.pincode,
        complete_address = address.complete_address,
        created_at = address.created_at


    )
    db.add(db_address)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_address)  # Refresh the user instance with the latest data from DB
    return db_address

def get_all_address(db:Session):
    return db.query(Address).all()


def delete_address(db:Session, address_id:int):
    address = db.query(Address).filter(Address.id == address_id). first()
    if address:
        db.delete(address)
        db.commit()
        return {"success": True, "message":"address deleted successfully"}
    return {"success":False,"message":"address not found"}

def update_address(db: Session, address_id: int, address_data: AddressUpdate):
    # Fetch product from the database (Product is the SQLAlchemy model)
    address = db.query(Address).filter(Address.id == address_id).first()

    if not address:
        raise HTTPException(status_code=404, detail="address not found")

# #    Update only provided fields
    address_data_dict = address_data.model_dump(exclude_unset=True)  # Use model_dump() for Pydantic v2

    for key, value in address_data_dict.items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)

    return {"message": "address updated successfully"}