from sqlalchemy.orm import Session
from api.database.models.review import Review
from api.database.schemas.review import ReviewCreate

def create_review(db: Session,  review: ReviewCreate):
    
    db_review = Review(

        user_id = review.user_id,
        order_id = review.order_id,
        product_id = review.product_id,
        rating = review.rating,
        review = review.review,
        created_at = review.created_at


    )
    db.add(db_review)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_review)  # Refresh the user instance with the latest data from DB
    return db_review

def get_all_review(db:Session):
    return db.query(Review).all()