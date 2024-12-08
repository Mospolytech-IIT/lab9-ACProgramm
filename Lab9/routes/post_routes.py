from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_post, get_all_posts, get_posts_by_user, update_post_content, delete_post
from models import Post
import uuid

router = APIRouter()

@router.post("/posts/")
def add_post(title: str, content: str, user_id: uuid.UUID, db: Session = Depends(get_db)):
    return create_post(db, title, content, user_id)

@router.get("/posts/")
def list_posts(db: Session = Depends(get_db)):
    return get_all_posts(db)

@router.get("/posts/user/{user_id}")
def list_user_posts(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_posts_by_user(db, user_id)

@router.put("/posts/{post_id}")
def edit_post_content(post_id: uuid.UUID, new_content: str, db: Session = Depends(get_db)):
    post = update_post_content(db, post_id, new_content)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/posts/{post_id}")
def remove_post(post_id: uuid.UUID, db: Session = Depends(get_db)):
    delete_post(db, post_id)
    return {"message": "Post deleted"}
