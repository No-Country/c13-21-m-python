from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    country: str


class UserCreate(UserBase):
    pass_user: str


class User(UserBase):
    user_id: int
    is_active: bool

    class Config:
        orm_mode = True
