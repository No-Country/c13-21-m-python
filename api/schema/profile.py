from pydantic import BaseModel
from schema.user import User


class ProfileBase(BaseModel):
    id: int
    name: str
    phone: str
    state: str
    province: str
    postal_code: str
    user_id: User

    class Config:
        from_attributes = True
        from_orm = True


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    pass
