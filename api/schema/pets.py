from pydantic import BaseModel

class PetBase(BaseModel):
    id: int
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
    publication_id: int

    class Config:
        from_attributes = True
        from_orm = True


class PetCreate(PetBase):
    pass


class Pet(PetBase):
    pass
