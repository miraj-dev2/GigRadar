from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class GigCreate(BaseModel):
    title: str
    description: str
    price: float

class GigOut(BaseModel):
    id: int
    title: str
    description: str
    price: float
    user_id: int

    class Config:
        from_attributes = True


class ApplicationCreate(BaseModel):
    gig_id: int
    status: str = "applied"
    notes: str | None = None


class ApplicationOut(BaseModel):
    id: int
    gig_id: int
    status: str
    notes: str | None
    applied_at: datetime

    class Config:
        from_attributes = True