from pydantic import BaseModel
from typing import Optional

class GradeCreate(BaseModel):
    student_id: str
    subject: str
    value: float
    date: Optional[str] = None

class GradeUpdate(BaseModel):
    student_id: Optional[str] = None
    subject: Optional[str] = None
    value: Optional[float] = None
    date: Optional[str] = None