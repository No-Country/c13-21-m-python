from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    user_id: Optional[int]
    email: str
    pass_user: str
    country: str

