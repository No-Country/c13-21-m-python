from typing import List, Optional
from pydantic import BaseModel
from model.user import CountryEnum
#from schema.publication import Publication
from schema.profile import Profile, ProfileDetails


class UserBase(BaseModel):
    email: str
    country: CountryEnum
    is_active: bool


class UserCreate(UserBase):
    pass_user: str


class User(UserBase):
    id: int
    publication_id: int
    #publication_user: List[Publication] = []
    #profile_user: Profile

    class Config:
        from_attributes = True
        from_orm = True


class UserDetails(BaseModel):
    profile_user: ProfileDetails


class UserUpdate(BaseModel):
    email: Optional[str]
    country: Optional[CountryEnum]
