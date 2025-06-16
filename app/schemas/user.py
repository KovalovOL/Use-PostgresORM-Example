from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str

class User(CreateUser):
    id: int