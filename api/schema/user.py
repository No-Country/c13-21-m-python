from pydantic import BaseModel
from model.user import CountryEnum
from schema.publication import Publication
from schema.profile import Profile


class User(BaseModel):
    id: int
    email: str
    country: CountryEnum
    is_active: bool
    publication_user: Publication
    profile_user: Profile


    class Config:
        from_attributes = True  # Habilita la conversión desde objetos ORM
        from_orm = True


class UserCreate(User):
    pass_user: str
