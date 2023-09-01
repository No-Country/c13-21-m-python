from pydantic import BaseModel


class ProfileBase(BaseModel):
    id: int
    name: str
    phone: str
    state: str
    province: str
    postal_code: str
    user_id: int

    class Config:
        from_attributes = True
        from_orm = True


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    pass
