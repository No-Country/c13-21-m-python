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
