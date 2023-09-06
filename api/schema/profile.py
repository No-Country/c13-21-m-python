from typing import Optional
from pydantic import BaseModel


class ProfileBase(BaseModel):
    name: str
    phone: str
    state: str
    province: str
    postal_code: str


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
        from_orm = True


class ProfileDetails(BaseModel):
    name: str
    phone: str


class ProfileUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    state: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]
