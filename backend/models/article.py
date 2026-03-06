from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Article(BaseModel):
    title: str
    description: Optional[str] = None
    content: Optional[str] = None
    url: str
    source: str
    published_at: datetime
    category: Optional[str] = None
    summary: Optional[str] = None
    sentiment: Optional[str] = None