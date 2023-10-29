from typing import Optional
from pydantic import BaseModel

class Posts(BaseModel):
    id: Optional[int]
    title: str
    content: str
    published: bool = True
    created_at: Optional[str]