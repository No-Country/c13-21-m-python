from pydantic import BaseModel


class Pets(BaseModel):
    id: int
    type: str
    name: str
    age: int
    genre: str
    size: str
    breed: str
    eye_color: str
    distinctive_feature: str
    fur: str
    necklace: bool

    class Config:
        from_attributes = True
        from_orm = True
