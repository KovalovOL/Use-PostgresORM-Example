from pydantic import BaseModel, Field
from typing import Optional

class CreateUser(BaseModel):
    name: str = Field(..., max_length=25)

class User(CreateUser):
    id: int

class UserFilter(BaseModel):
    id: Optional[int] = Field(None, ge=0)
    name: Optional[str] = Field(None, max_length=25)