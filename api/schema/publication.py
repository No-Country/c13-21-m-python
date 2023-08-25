from pydantic import BaseModel
from typing import List
from schema.image_publication import ImagesInPublication
from schema.user import User
from schema.pets import Pets


class PublicationBase(BaseModel):
    publication_date: str
    pub_type: List[str]
    city: str
    address: str | None = None


class PublicationCreate(PublicationBase):
    pass


class Publication(PublicationBase):
    publication_id: int
    # images: list[ImagesInPublication] = []
    # publications_by_user: list[User] = []
    # pets: list[Pets] = []

    class Config:
        orm_mode = True
