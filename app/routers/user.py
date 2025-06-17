from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas import user as user_schemas
from app.crud import user as user_crud


router = APIRouter()


@router.get("/")
async def get_user(
    user_id: int = Query(None, ge=0),
    name: str = Query(None, max_length=25),
    db: Session = Depends(get_db)) -> List[user_schemas.User]:

    filter = user_schemas.UserFilter(
        id=user_id,
        name=name
    )

    return user_crud.get_user(db=db, filter=filter)

@router.post("/")
async def create_user(user: user_schemas.CreateUser, db: Session = Depends(get_db)) -> user_schemas.User:
    return user_crud.create_user(db=db, user=user)

@router.delete("/{user_id}")
async def delete_user(user_id: int = Path(..., ge=0), db: Session = Depends(get_db)) -> user_schemas.User:
    return user_crud.delete_user(db=db, user_id=user_id)