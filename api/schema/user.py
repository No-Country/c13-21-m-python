from typing import List
from pydantic import BaseModel
from model.user import CountryEnum
from schema.publication import Publication
from schema.profile import Profile


class UserBase(BaseModel):
    email: str
    country: CountryEnum
    is_active: bool


class UserCreate(UserBase):
    pass_user: str


class User(UserBase):
    id: int
    publication_user: List[Publication] = []
    profile_user: Profile

    class Config:
        from_attributes = True  # Habilita la conversión desde objetos ORM
        from_orm = True
