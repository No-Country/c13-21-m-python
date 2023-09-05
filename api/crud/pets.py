from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from model.pets import Pet
from schema.pets import PetCreate, PetUpdate


def get_by_id(id:int, db:Session):
    pet = db.query(Pet).get(id)

    if pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return pet


def create(pet: PetCreate):
    db_pet_publication = Pet(
        type = pet.type,
        name = pet.name,
        age = pet.age,
        genre = pet.genre,
        size = pet.size,
        breed = pet.breed,
        eye_color = pet.eye_color,
        description = pet.description,
        fur = pet.fur,
        necklace = pet.necklace,
        color = pet.color
        )
    return db_pet_publication


def update(id: int, db: Session, pet: PetUpdate):
    db_pet = get_by_id(id, db)
    if not db_pet:
         raise HTTPException(status_code=404, detail="Pet not found")
    pet_data = pet.dict(exclude_unset=True)
    for key, value in pet_data.items():
         setattr(db_pet, key, value)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet
