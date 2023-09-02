from pydantic import BaseModel
from model.user import CountryEnum


class User(BaseModel):
    id: int
    email: str
    country: CountryEnum
    is_active: bool


    class Config:
        from_attributes = True  # Habilita la conversión desde objetos ORM
        from_orm = True


class UserCreate(User):
    pass_user: str
