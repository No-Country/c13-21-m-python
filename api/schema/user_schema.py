from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    user_id: Optional[int] = None
    email: EmailStr
    pass_user: str
    country: str
    is_active: bool

    class Config:
        from_attributes = True