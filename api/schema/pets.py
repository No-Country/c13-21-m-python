from pydantic import BaseModel


class PetBase(BaseModel):
    type: str
    name: str
    age: int
    genre: str
    size: str
    breed: str
    eye_color: str
    description: str
    fur: str
    necklace: bool
    color: str



class PetCreate(PetBase):
    pass


class Pet(PetBase):
    id: int
    publication_id: int


    class Config:
        from_attributes = True
        from_orm = True
