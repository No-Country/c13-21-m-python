from pydantic import BaseModel
from schema.user import User


class ProfileBase(BaseModel):
    name: str
    phone: str
    state: str
    province: str
    postal_code: str

    class Config:
        from_attributes = True
        from_orm = True

class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    profile_id: int
    user_id: int
    users: list[User]
