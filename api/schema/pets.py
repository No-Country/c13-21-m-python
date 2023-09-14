from typing import Optional
from pydantic import BaseModel
from enum import Enum

class TypeEnum(str, Enum):
    Perro = "Perro"
    Gato = "Gato"
    Hamster = "Hamster"
    Conejo = "Conejo"
    Tortuga = "Tortuga"

class GenreEnum(str, Enum):
    macho = "macho"
    hembra = "hembra"

class ColorEnum(str, Enum):
    blanco = "blanco"
    azul = "azul"
    negro = "negro"
    gris = "gris"
    verde = "verde"
    amarillo = "amarillo"
    bicolor = "bicolor"
    atigrado = "atigrado"
    cafe = "cafe"
    miel = "miel"
    marron = "marron"
    tricolor = "tricolor"

class FurEnum(str, Enum):
    fino = "fino"
    chino = "chino"
    maltratado = "maltratado"
    grueso = "grueso"
    corto = "corto"
    largo = "largo"
    NA = "NA"

class SizeEnum(str, Enum):
    pequeña = "pequeña"
    chica = "chica"
    mediana = "mediana"
    grande = "grande"

class PetBase(BaseModel):
    type: TypeEnum
    name: str
    age: int
    genre: GenreEnum
    size: SizeEnum
    breed: str
    eye_color: ColorEnum
    description: str
    fur: FurEnum
    necklace: bool
    color: ColorEnum

    class Config:
        from_attributes = True
        from_orm = True

class PetCreate(PetBase):
    pass


class Pet(PetBase):
    id: int
    publication_id: int


    class Config:
        from_attributes = True
        from_orm = True


class PetUpdate(BaseModel):
    type: Optional[TypeEnum] = None
    name: Optional[str] = None
    age: Optional[int] = None
    genre: Optional[GenreEnum] = None
    size: Optional[SizeEnum] = None
    breed: Optional[str] = None
    eye_color: Optional[ColorEnum] = None
    description: Optional[str] = None
    fur: Optional[FurEnum] = None
    necklace: Optional[bool] = None
    color: Optional[ColorEnum] = None


class PetSlider(BaseModel):
    name: str


class PetView(BaseModel):
    type: TypeEnum
    name: str
    genre: GenreEnum
    description: str


class PetDetails(BaseModel):
    type: TypeEnum
    name: str
    genre: GenreEnum
    description: str
