from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query, Path
from datetime import datetime
from typing import List

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
    time_create: datetime = Query(None),
    db: Session = Depends(get_db)) -> List[post_schemas.Post]:

    filter = post_schemas.PostFilter(
        post_id=post_id,
        user_id=user_id,
        title=title,
        time_create=time_create
    )

    return post_crud.get_post(db=db, filter=filter)

@router.post("/")
async def create_post(post: post_schemas.CreatePost, db: Session = Depends(get_db)) -> post_schemas.Post:
    return post_crud.create_post(db=db, post=post)

@router.put("/{post_id}")
async def update_user(
    data: post_schemas.UpdatePost,
    post_id: int = Path(..., ge=0),
    db: Session = Depends(get_db)) -> post_schemas.Post:

    return post_crud.update_post(db=db, post_id=post_id, post_update=data)

@router.delete("/{post_id}")
async def delete_post(post_id: int = Path(..., ge=0), db: Session = Depends(get_db)) -> post_schemas.Post:
    return post_crud.delete_post(db=db, post_id=post_id)
