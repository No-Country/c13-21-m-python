from config.database import Base, SessionLocal, engine
from fastapi import (
    Depends,
    FastAPI,
    Query,
    Path,
    APIRouter,
    status,
    Body,
    HTTPException,
    File,
    UploadFile,
)
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination

from crud import (
    image_publication as crudImagePublication,
    profile as crudProfile,
    publication as crudPublication,
    user as crudUser,
    pets as crudPet,
    upload as crudUpload,
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
from fastapi.middleware.cors import CORSMiddleware

# from fastapi_cognito import CognitoAuth, CognitoSettings
# from schema.userpool import settings
# from fastapi_cognito import CognitoToken

# default userpool(eu) will be used if there is no userpool_name param provided.
# cognito_us = CognitoAuth(
#   settings=CognitoSettings.from_global_settings(settings), userpool_name="petfinder-userpool"
# )

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

# CORS configuration
#origins = [
#    "http://localhost",
#    "http://localhost:3000",  # Replace with your frontend's origin
#    "http://50.18.105.237:50",
#    "http://50.18.105.237:50:5000"
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods here
    allow_headers=["*"],  # You can specify specific headers here
)


router = APIRouter()


# Routers image_publication
@app.get("/api/imagePublication/{id}", status_code=status.HTTP_200_OK)
def get_imagePublication_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    image_publication = crudImagePublication.get_by_id(id, db)
    return {"image_publication": image_publication}


@app.patch("/api/imagePublication/{id}", status_code=status.HTTP_200_OK)
def update_image_publication(
    id: int = Path(...),
    image_publication: schemaImagePublication.ImageInPublicationUpdate = Body(...),
    db: Session = Depends(get_db),
):
    image_publication_result = crudImagePublication.update(id, db, image_publication)
    return {"image_publication": image_publication_result}


# Routers pet
@app.get("/api/pets/{id}", status_code=status.HTTP_200_OK)
def get_pet_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    pet = crudPet.get_by_id(id, db)
    return {"pet": pet}


@app.patch("/api/pets/{id}", status_code=status.HTTP_200_OK)
def update_pet(
    id: int = Path(...),
    pet: schemaPets.PetUpdate = Body(...),
    db: Session = Depends(get_db),
):
    pet_result = crudPet.update(id, db, pet)
    return {"publication": pet_result}


# Routers publication
@app.get("/api/publications/{id}", status_code=status.HTTP_200_OK)
def get_publication_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    publication = crudPublication.get_by_id(id, db)
    return {"publication": publication}


@app.get(
    "/api/carouselPerdidos/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationCarousel],
)
def get_carousel_perdidos(db: Session = Depends(get_db)):
    return crudPublication.get_carouselPerdidos(db)


@app.get(
    "/api/carouselEncontrados/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationCarousel],
)
def get_carousel_encontrados(db: Session = Depends(get_db)):
    return crudPublication.get_carouselEncontrados(db)


@app.get(
    "/api/carouselAdopciones/",
    status_code=status.HTTP_200_OK,
    response_model=Page[schemaPublication.PublicationCarousel],
)
def get_carousel_adopciones(db: Session = Depends(get_db)):
    return crudPublication.get_carouselAdopciones(db)


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


@app.post("/api/upload-image", response_model=schemaImagePublication.UploadedImage)
def upload_and_get_image_data(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    image_name, url_image = crudUpload.upload_image(file, db)

    return {"image": image_name, "url": url_image}


@app.post("/api/publications", status_code=status.HTTP_201_CREATED)
def add_publication(
    publication: schemaPublication.PublicationCreate,
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.create(publication, db)

    return {"publication": publication_result}


@app.patch("/api/publications/{id}", status_code=status.HTTP_200_OK)
def update_publication(
    id: int = Path(...),
    publication: schemaPublication.PublicationUpdate = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.update(id, db, publication)
    return {"publication": publication_result}


@app.delete("/api/publications/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publication(id: int = Path(...), db: Session = Depends(get_db)):
    crudPublication.delete(id, db)


# Routers user
# @app.get("/api/users/{id}", status_code=status.HTTP_200_OK)
# def get_user_by_id(id: int = Path(...), db: Session = Depends(get_db)):
#     user = crudUser.get_by_id(id, db)
#     return {"user": user}


# @app.get("/api/users/", status_code=status.HTTP_200_OK)
# def get_users(db: Session = Depends(get_db)):
#     users = crudUser.get_all(db)
#     return {"users": users}


# @app.get("/api/user/publications/{id}", status_code=status.HTTP_200_OK)
# def get_publications_user(id: int, db: Session = Depends(get_db)):
#     users = crudUser.get_publications(id, db)
#     return {"users": users}

# anterior
# @app.post("/api/users/", status_code=status.HTTP_201_CREATED)
# def add_user(user: schemaUser.UserCreate = Body(...), db: Session = Depends(get_db)):
#     user_result = crudUser.create(user, db)
#     return {"user": user_result}


# @app.patch("/api/users/{id}", status_code=status.HTTP_200_OK)
# def update_user(
#     id: int = Path(...),
#     user: schemaUser.UserUpdate = Body(...),
#     db: Session = Depends(get_db),
# ):
#     user_result = crudUser.update(id, db, user)
#     return {"user": user_result}


# @app.delete("/api/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(id: int = Path(...), db: Session = Depends(get_db)):
#     crudUser.delete(id, db)


# @app.post("/api/users/", status_code=status.HTTP_201_CREATED)
# def register_user(user: schemaUser.UserCreate, db: Session = Depends(get_db)):
#     user_result = crudUser.create(user, db)
#     return {"user": user_result}

# Routers profile
# @app.post("/api/createProfile/", status_code=status.HTTP_201_CREATED)
# def add_profile(
#     profile: schemaProfile.ProfileCreate = Body(...), db: Session = Depends(get_db)
# ):
#     profile_result = crudProfile.create(profile, db)
#     return {"profile": profile_result}


# @app.patch("/api/profile/{id}", status_code=status.HTTP_200_OK)
# def update_profile(
#     id: int = Path(...),
#     profile: schemaProfile.ProfileUpdate = Body(...),
#     db: Session = Depends(get_db),
# ):
#     profile_result = crudProfile.update(id, db, profile)
#     return {"profile": profile_result}
