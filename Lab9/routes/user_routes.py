from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_user, get_all_users, update_user_email, delete_user_and_posts
from models import User
import uuid

router = APIRouter()

@router.post("/users/")
def add_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

@router.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.put("/users/{user_id}")
def edit_user_email(user_id: uuid.UUID, new_email: str, db: Session = Depends(get_db)):
    user = update_user_email(db, user_id, new_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
def remove_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    delete_user_and_posts(db, user_id)
    return {"message": "User and their posts deleted"}
