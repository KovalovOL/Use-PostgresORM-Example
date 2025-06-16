from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.database import get_db
from app.db import models
from app.schemas import post as post_schemas
from app.crud import post as post_crud


router = APIRouter()


@router.get("/")
async def get_post(
    post_id: int = Query(None, ge=0),
    user_id: int = Query(None, ge=0),
    title: str = Query(None, max_length=50),
    time: datetime = Query(None), 
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

@router.delete("/{post_id}")
async def delete_post(post_id: int = Path(..., ge=0), db: Session = Depends(get_db)):
    return post_crud.delete_post(db=db, post_id=post_id)
