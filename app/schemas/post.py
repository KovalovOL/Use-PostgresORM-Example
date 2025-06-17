from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CreatePost(BaseModel):
    title: str = Field(..., max_length=50)
    text: str = Field(..., max_length=200)
    user_id: int

class Post(CreatePost):
    id: int
    time_create: datetime

class PostFilter(BaseModel):
    post_id: Optional[int] = Field(None, ge=0)
    user_id: Optional[int] = Field(None, ge=0)
    title: Optional[str] = Field(None, max_length=50)
    time_create: Optional[datetime] = Field(None)
