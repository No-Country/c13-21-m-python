from pydantic import BaseModel
from typing import Optional

class PetSchema(BaseModel):
    pet_id: Optional[int]
    type: Optional[str]
    name: Optional[str]
    age: Optional[int]
    genre: str
    size: str
    breed: Optional[str]
    eye_color: str
    distinctive_feature: Optional[str]
    colors: list
    publication_id: int