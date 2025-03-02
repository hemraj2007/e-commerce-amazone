from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.product import Product
from api.database.schemas.product import ProductCreate,ProductUpdate

def create_product(db: Session,  product: ProductCreate):
    
    db_product = Product(


        category_id = product.category_id,
        name = product.name,
        description = product.description,
        mrp = product.mrp,
        net_price = product.net_price,
        quantity_in_stock = product.quantity_in_stock,
        image = product.image,
        status = product.status,
        created_at = product.created_at,
        updated_at = product.updated_at,
       
        

    )
    db.add(db_product)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_product)  # Refresh the user instance with the latest data from DB
    return db_product


def get_all_products(db:Session):
    return db.query(Product).all()


def delete_product(db:Session, product_id:int):
    product = db.query(Product).filter(Product.id == product_id). first()
    if product:
        db.delete(product)
        db.commit()
        return {"success": True, "message":"product deleted successfully"}
    return {"success":False,"message":"product not found"}


def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    # Fetch product from the database (Product is the SQLAlchemy model)
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

# #    Update only provided fields
    product_data_dict = product_data.model_dump(exclude_unset=True)  # Use model_dump() for Pydantic v2

    for key, value in product_data_dict.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return {"message": "Product updated successfully"}