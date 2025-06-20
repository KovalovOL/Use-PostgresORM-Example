from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db import models
from app.schemas import post as post_schemas


def get_post(db: Session, filter: post_schemas.PostFilter):
    conditions = []

    if filter.post_id is not None: conditions.append(models.Post.id == filter.post_id)
    if filter.user_id is not None: conditions.append(models.Post.user_id == filter.user_id)
    if filter.title is not None: conditions.append(models.Post.title.ilike(f"%{filter.title}%"))
    if filter.time_create is not None: conditions.append(models.Post.time_create >= filter.time_create)

    return db.query(models.Post).filter(*conditions).all()

def create_post(db: Session, post: post_schemas.CreatePost):
    db_post = models.Post(
        title=post.title,
        text=post.text,
        user_id=post.user_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post_update: post_schemas.UpdatePost):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    
    if post_update.new_title is not None:
        post.title = post_update.new_title
    if post_update.new_text is not None:
        post.text = post_update.new_text
    if post_update.new_user_id is not None:
        if db.query(models.User).filter(models.User.id == post_update.new_user_id).first():
            post.user_id = post_update.new_user_id
        else:
            raise HTTPException(status_code=404, detail=f"User with id {post_update.new_user_id} not found")
    
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post