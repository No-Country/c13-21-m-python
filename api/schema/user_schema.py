from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    user_id: Optional[int]
    email: EmailStr
    password: str
    country: str