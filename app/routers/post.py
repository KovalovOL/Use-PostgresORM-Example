from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.db.database import get_db
from app.db import models
from app.schemas import post as post_schemas
from app.crud import post as post_crud

router = APIRouter()


@router.get("/")
async def get_post(
    post_id: Optional[int] = None,
    user_id: Optional[int] = None,
    title: Optional[str] = None,
    time: Optional[datetime] = None, 
    db: Session = Depends(get_db)):

   filters = []

   if post_id is not None: filters.append(models.Post.id == post_id)
   if user_id is not None: filters.append(models.Post.user_id == user_id)
   if title is not None: filters.append(models.Post.title.ilike(f"%{title}%"))
   if time is not None: filters.append(models.Post.time_create >= time) 

   return db.query(models.Post).filter(*filters).all()

@router.post("/")
async def create_post(post: post_schemas.CreatePost, db: Session = Depends(get_db)):
    return post_crud.create_post(db=db, post=post)

@router.delete("/")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    return post_crud.delete_post(db=db, post_id=post_id)
