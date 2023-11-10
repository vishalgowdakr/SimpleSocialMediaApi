from pydantic import BaseModel, EmailStr
from datetime import datetime


class Posts(BaseModel):
    title: str
    content: str
    published: bool = True

class GetPost(Posts):
    id: int
    created_at: datetime

class createUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class loginUser(BaseModel):
    username: str
    password: str
    
class getUser(BaseModel):
    username: str
    email: EmailStr

    
