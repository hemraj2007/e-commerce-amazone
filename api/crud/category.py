from sqlalchemy.orm import Session
from api.database.models.category import Category
from api.database.schemas.category import CategoryCreate

def create_category(db: Session,  category: CategoryCreate):
    
    
    db_category = Category(

        name = category.name,
        created_at = category.created_at,
        updated_at = category.updated_at

        
    )
    db.add(db_category)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_category)  # Refresh the user instance with the latest data from DB
    return db_category


def get_all_category(db:Session):
    return db.query(Category).all()



def delete_category(db:Session, category_id:int):
    category = db.query(Category).filter(Category.id == category_id). first()
    if category:
        db.delete(category)
        db.commit()
        return {"success": True, "message":"category deleted successfully"}
    return {"success":False,"message":"category not found"}
