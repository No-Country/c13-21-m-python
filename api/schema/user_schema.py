from pydantic import BaseModel, EmailStr
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    user_id: Optional[int]
    email: EmailStr
    pass_user: str
    country: str
