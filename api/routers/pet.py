from fastapi import APIRouter
from enum import Enum

pet_router = APIRouter()

pet_list = []

class GenreType(str, Enum):
    M = "macho"
    H = "hembra"

class SizeType(str, Enum):
    P = "pequeña"
    C = "chica"
    M = "mediana"
    G = "grande"


@pet_router.get("/")
def get():
    return {"pets": pet_list}

@pet_router.post("/{pet}")
def add(pet):
    pet_list.append(pet)
    return {"pets": pet_list}

@pet_router.put("/")
def update(index: int, pet: str):
    pet_list[index] = pet
    return {"pets": pet_list}

@pet_router.delete("/")
def delete(index: int):
    del pet_list[index]
    return {"pets": pet_list}

# @pet_router.get("/")
# def get():
#     return {"pet": "pet"}