from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class UserBase(BaseModel):
    email: str
    role: Enum


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True