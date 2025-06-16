from pydantic import BaseModel
from datetime import datetime

class CreatePost(BaseModel):
    title: str
    text: str
    user_id: int

class Post(CreatePost):
    id: int
    time_create: datetime
