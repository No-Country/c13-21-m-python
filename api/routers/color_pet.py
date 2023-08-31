from fastapi import APIRouter

color_pet_router = APIRouter()

color_pet_list = []

@color_pet_router.get("/")
def get():
    return {"color_pets": color_pet_list}

@color_pet_router.post("/{color_pet}")
def add(color_pet):
    color_pet_list.append(color_pet)
    return {"color_pets": color_pet_list}

@color_pet_router.put("/")
def update(index: int, color_pet: str):
    color_pet_list[index] = color_pet
    return {"color_pets": color_pet_list}

@color_pet_router.delete("/")
def delete(index: int):
    del color_pet_list[index]
    return {"color_pets": color_pet_list}

# @color_pet_router.get("/")
# def get():
#     return {"color_pet": "color_pet"}