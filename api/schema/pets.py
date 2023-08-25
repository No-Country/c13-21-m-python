from pydantic import BaseModel
from schema.colors_pet import ColorsPet


class PetsBase(BaseModel):
    type: str
    name: str
    age: int
    genre: str
    size: str
    breed: str
    eye_color: str
    distinctive_feature: str


class PetsCreate(PetsBase):
    pass


class Pets(PetsBase):
    pet_id: int
    colors_pet_id: int
    colors: list[ColorsPet]

    class Config:
        orm_mode = True
