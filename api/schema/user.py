from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass_user: str


class User(UserBase):
    user_id: int
    is_active: bool
    country: str

    class Config:
        orm_mode = True
