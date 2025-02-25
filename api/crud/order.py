from sqlalchemy.orm import Session
from api.database.models.order import Order
from api.database.schemas.order import OrderCreate

def create_order(db: Session,  order: OrderCreate):
    
    db_order = Order(


        user_id = order.user_id,
        subtotal = order.subtotal,
        discount = order.discount,
        total = order.total,
        status = order.status,
        shipping_address = order.shipping_address,
        created_at = order.created_at,
        updated_at = order.updated_at,

    )
    db.add(db_order)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_order)  # Refresh the user instance with the latest data from DB
    return db_order

def get_all_address(db:Session):
    return db.query(Order).all()