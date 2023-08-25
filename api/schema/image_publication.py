from pydantic import BaseModel


class ImageInPublicationBase(BaseModel):
    image: str


class ImageInPublicationCreate(ImageInPublicationBase):
    pass


class ImagesInPublication(ImageInPublicationBase):
    image_publication_id: int

    class Config:
        orm_mode = True
