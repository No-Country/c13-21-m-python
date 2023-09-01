from pydantic import BaseModel, HttpUrl


class ImageInPublicationBase(BaseModel):
    id: int
    image: str
    url: str
    publication_id: int

    class Config:
        from_attributes = True
        from_orm = True


class ImageInPublicationCreate(ImageInPublicationBase):
    pass


class ImagesInPublication(ImageInPublicationBase):
    pass
