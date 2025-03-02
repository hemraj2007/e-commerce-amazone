from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.user import UserResponse
from api.database.schemas.user import  UserPasswordUpdate
from api.token import get_current_user
from api.crud.user import get_user_by_email,update_user_password

# ✅ Single router instance
router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    """
    API endpoint to get user profile.
    """
    return current_user


@router.put("/update-password")
def update_password(
    email:str,
    password_data: UserPasswordUpdate, 
    db: Session = Depends(get_db)
    ):

    # Fetch user by email
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if new password matches confirm password
    if password_data.new_password != password_data.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirmation password do not match")

    # Update password in database
    update_user_password(db, password_data)

    return {"message": "Password updated successfully"}
