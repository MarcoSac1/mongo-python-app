from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    title: str
    category: str
    description: Optional[str] = None
    active: bool = True


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None
