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

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post