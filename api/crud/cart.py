from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.cart import Cart
from api.database.schemas.cart import CartCreate,CartUpdate


def create_cart(db: Session,  cart: CartCreate):
    
    db_cart = Cart(
        user_id = cart.user_id,
        product_id = cart.product_id,
        quantity = cart.quantity,
        created_at = cart.created_at

        

    )
    db.add(db_cart)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_cart)  # Refresh the user instance with the latest data from DB
    return db_cart


def get_all_cart(db:Session):
    return db.query(Cart).all()

def delete_cart(db:Session, cart_id:int):
    cart = db.query(Cart).filter(Cart.id == cart_id). first()
    if cart:
        db.delete(cart)
        db.commit()
        return {"success": True, "message":"cart deleted successfully"}
    return {"success":False,"message":"cart not found"}


def update_cart(db: Session, cart_id: int, cart_data: CartUpdate):
    # Fetch product from the database (Product is the SQLAlchemy model)
    cart = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="cart not found")

# #    Update only provided fields
    cart_data_dict = cart_data.model_dump(exclude_unset=True)  # Use model_dump() for Pydantic v2

    for key, value in cart_data_dict.items():
        setattr(cart, key, value)

    db.commit()
    db.refresh(cart)

    return {"message": "cart updated successfully"}