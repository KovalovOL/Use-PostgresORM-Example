from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    name: str = Field(..., max_length=25)

class User(CreateUser):
    id: int