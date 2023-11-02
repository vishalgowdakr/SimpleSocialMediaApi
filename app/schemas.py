from typing import Optional
from pydantic import BaseModel


class Posts(BaseModel):
    title: str
    content: str
    published: bool = True

