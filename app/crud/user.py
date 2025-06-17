from sqlalchemy.orm import Session
from app.db import models
from app.schemas import user as user_schemas


def get_user(db: Session, filter: user_schemas.UserFilter):
    conditions = []

    if filter.id is not None: conditions.append(models.User.id == filter.id)
    if filter.name is not None: conditions.append(models.User.name == filter.name)

    return db.query(models.User).filter(*conditions).all()

def create_user(db: Session, user: user_schemas.CreateUser):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
    