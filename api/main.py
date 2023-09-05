from config.database import Base, SessionLocal, engine
from fastapi import Depends, FastAPI, Query, Path, APIRouter, status, Body
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination

from crud import (
    image_publication as crudImagePublication,
    profile as crudProfile,
    publication as crudPublication,
    user as crudUser,
)
from model import (
    image_publication as modelImagePublication,
    pets as modelPets,
    profile as modelProfile,
    publication as modelPublication,
    user as modelUser,
)
from schema import (
    image_publication as schemaImagePublication,
    pets as schemaPets,
    profile as schemaProfile,
    publication as schemaPublication,
    user as schemaUser,
)

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
add_pagination(app)


router = APIRouter()


# Routers image_publication
@app.get("/api/images_publication/{id}", status_code=status.HTTP_200_OK)
def get_image_by_id(db: Session = Depends(get_db)):
    image_publication = crudImagePublication.get_by_id(db=db, id=id)
    return image_publication


@app.get("/api/images_publication/", status_code=status.HTTP_200_OK)
def get_images(db: Session = Depends(get_db)):
    image_publications = crudImagePublication.get_all(db=db)
    return image_publications


@app.post("/api/images_publication/")
def add_image(
    image_publication: schemaImagePublication.ImageInPublicationCreate,
    db: Session = Depends(get_db),
):
    image_publication_result = crudImagePublication.create(image_publication, db)
    return image_publication_result


@app.put("/api/images_publication/")
def update_image(index: int, image_publication: str, db: Session = Depends(get_db)):
    # publication_list[index] = publication
    # return {"publications": publication_list}
    pass


@app.delete("/api/images_publication/")
def delete_image(index: int, db: Session = Depends(get_db)):
    # del publication_list[index]
    # return {"publications": publication_list}
    pass


# Routers pets
pet_list = []


@app.get("/api/pets/")
def get_pets():
    return {"pets": pet_list}


@app.post("/api/pets/{pet}")
def add_pet(pet):
    pet_list.append(pet)
    return {"pets": pet_list}


@app.put("/api/pets/")
def update_pet(index: int, pet: str):
    pet_list[index] = pet
    return {"pets": pet_list}


@app.delete("/api/pets/")
def delete_pet(index: int):
    del pet_list[index]
    return {"pets": pet_list}


# Routers publication
@app.get("/api/publications/{id}", status_code=status.HTTP_200_OK)
def get_publication_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    publication = crudPublication.get_by_id(db, id)
    return {"publication": publication}


@app.get(
    "/api/sliderPerdidos/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationSlider],
)
def get_slider_perdidos(db: Session = Depends(get_db)):
    return crudPublication.get_sliderPerdidos(db)


@app.get(
    "/api/sliderEncontrados/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationSlider],
)
def get_slider_encontrados(db: Session = Depends(get_db)):
    return crudPublication.get_sliderEncontrados(db)


@app.get(
    "/api/sliderAdopciones/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationSlider],
)
def get_slider_adopciones(db: Session = Depends(get_db)):
    return crudPublication.get_sliderAdopciones(db)


@app.get(
    "/api/viewPerdidos/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationView],
)
def get_view_perdidos(db: Session = Depends(get_db)):
    return crudPublication.get_viewPerdidos(db)


@app.get(
    "/api/viewEncontrados/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationView],
)
def get_view_encontrados(db: Session = Depends(get_db)):
    return crudPublication.get_viewEncontrados(db)


@app.get(
    "/api/viewAdopciones/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationView],
)
def get_view_adopciones(db: Session = Depends(get_db)):
    return crudPublication.get_viewAdopciones(db)


# @app.get(
#     "/api/publications/{id}",
#     status_code=status.HTTP_200_OK,
#     response_model=schemaPublication.PublicationDetails,
# )
# def get_details_publication(id: int = Path(...), db: Session = Depends(get_db)):
#     return crudPublication.get_detailsPublication(id, db)


@app.get(
    "/api/publications/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.Publication],
)
def get_publications(db: Session = Depends(get_db)):
    return crudPublication.get_all(db)


@app.post("/api/publications/", status_code=status.HTTP_201_CREATED)
def add_publication(
    publication: schemaPublication.Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.crud_create(publication, db)
    return {"publication": publication_result}


@app.put("/api/publications/{id}", status_code=status.HTTP_200_OK)
def update_publication(
    id: int = Path(...),
    publication: schemaPublication.Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.crud_update(id, db, publication)
    return {"publication": publication_result}


@app.delete("/api/publications/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publication(id: int = Path(...), db: Session = Depends(get_db)):
    crudPublication.crud_delete(id, db)


# Routers user
@app.get("/api/users/{id}", status_code=status.HTTP_200_OK)
def get_user_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    user = crudUser.get_by_id(db=db, id=id)
    return {"user": user}


@app.get("/api/users/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = crudUser.get_all(db=db)
    return {"users": users}


@app.post("/api/users/", status_code=status.HTTP_201_CREATED)
def add_user(
    user: schemaUser.User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crudUser.crud_create(user, db)
    return {"user": user_result}


@app.put("/api/users/{id}", status_code=status.HTTP_200_OK)
def update_user(
    id: int = Path(...),
    user: schemaUser.User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crudUser.crud_update(id, db, user)
    return {"user": user_result}


@app.delete("/api/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int = Path(...), db: Session = Depends(get_db)):
    crudUser.crud_delete(id, db)
