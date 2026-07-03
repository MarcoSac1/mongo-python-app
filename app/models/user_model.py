from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    city: Optional[str] = None
    active: bool = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    active: Optional[bool] = None

