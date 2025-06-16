from pydantic import BaseModel, Field
from datetime import datetime

class CreatePost(BaseModel):
    title: str = Field(..., max_length=50)
    text: str = Field(..., max_length=200)
    user_id: int

class Post(CreatePost):
    id: int
    time_create: datetime
