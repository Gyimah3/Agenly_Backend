from pydantic import BaseModel, EmailStr, Field

from typing import Optional, List
from datetime import datetime

# TokenData schema for JWT payload handling
class TokenData(BaseModel):
    user_id: Optional[int] = None

# Base user schema for common user properties
# class UserBase(BaseModel):
#     email: EmailStr
#     name: Optional[str] = None

# # Schema for creating a new user, inherits from UserBase and adds password
# class UserCreate(UserBase):
#     password: str

# # Schema for reading user data, inherits from UserBase and adds additional fields
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list = []  # If you have a specific item schema, you can specify List[ItemSchema] instead

#     class Config:
#         from_attributes = True  # Updated according to Pydantic 2.0+

# Define other schemas following the same pattern+
class UserBase(BaseModel):
    email: EmailStr  # Required field
    name: str  # Required field

class UserCreate(UserBase):
    password: str  # Required field
    phone: str  # Required field

class User(UserBase):
    id: int
    is_active: bool = True
    avatar_url: Optional[str] = None
    phone: str  # Required field
    website: Optional[str] = None
    role: Optional[str] = None
    permissions: Optional[str] = None
    notifications: Optional[bool] = None

    class Config:
        from_attributes = True
