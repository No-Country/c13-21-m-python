from typing import Optional
from pydantic import BaseModel


class ImageInPublicationBase(BaseModel):
    image: str
    url: str


class ImageInPublicationCreate(ImageInPublicationBase):
    pass


class ImagesInPublication(ImageInPublicationBase):
    id: int
    publication_id: int

    class Config:
        from_attributes = True
        from_orm = True


class ImageInPublicationUpdate(BaseModel):
    image: Optional[str] = None
    url: Optional[str] = None


class ImagesInPublicationSlider(BaseModel):
    url: str


class ImagesInPublicationView(BaseModel):
    url: str


class ImagesInPublicationDetails(BaseModel):
    url: str
