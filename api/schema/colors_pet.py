from pydantic import BaseModel


class ColorsPetBase(BaseModel):
    color: str


class ColorsPetCreate(ColorsPetBase):
    pass


class ColorsPet(ColorsPetBase):
    colors_pet_id: int
    pet_id: int

    class Config:
        orm_mode = True
