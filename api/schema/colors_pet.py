from pydantic import BaseModel


class ColorsPetBase(BaseModel):
    color: str

    class Config:
        from_attributes = True
        from_orm = True


class ColorsPetCreate(ColorsPetBase):
    pass


class ColorsPet(ColorsPetBase):
    colors_pet_id: int

    class Config:
        from_attributes = True
