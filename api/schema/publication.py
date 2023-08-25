from pydantic import BaseModel
from schema.image_publication import ImagesInPublication
from schema.publication_user import PublicationsByUser
from schema.pets import Pets


class PublicationBase(BaseModel):
    title: str
    description: str | None = None


class PublicationCreate(PublicationBase):
    pass


class Publication(PublicationBase):
    id: int
    owner_id: int
    images: list[ImagesInPublication] = []
    publications_by_user: list[PublicationsByUser] = []
    pets: list[Pets] = []

    class Config:
        orm_mode = True
