from typing import Optional
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


class PetUpdate(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
    genre: Optional[str] = None
    size: Optional[str] = None
    breed: Optional[str] = None
    eye_color: Optional[str] = None
    description: Optional[str] = None
    fur: Optional[str] = None
    necklace: Optional[bool] = None
    color: Optional[str] = None


class PetSlider(BaseModel):
    name: str


class PetView(BaseModel):
    type: str
    name: str
    genre: str
    description: str


class PetDetails(BaseModel):
    type: str
    name: str
    genre: str
    description: str
