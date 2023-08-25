from pydantic import BaseModel


class PublicationsByUserBase(BaseModel):
    pass


class PublicationsByUserCreate(PublicationsByUserBase):
    pass


class PublicationsByUser(PublicationsByUserBase):
    publications_user_id: int
    user_id: int

    class Config:
        orm_mode = True
