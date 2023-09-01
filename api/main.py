from config.database import Base, SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Query, Path, APIRouter, status, Body
from sqlalchemy.orm import Session
#from routers.publication import publication_router
#from routers.user import user_router
#from routers.image_publication import image_publication_router
#from routers.pet import pet_router
#from routers.profile import profile_router
#from routers.upload import upload_router

from crud import image_publication as crudImagePublication, profile as crudProfile, publication as crudPublication, user as crudUser
from model import image_publication as modelImagePublication, pets as modelPets, profile as modelProfile, publication as modelPublication, user as modelUser
from schema import image_publication as schemaImagePublication, pets as schemaPets, profile as schemaProfile, publication as schemaPublication, user as schemaUser

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

router = APIRouter()





@app.get("/e_page")
def page(
    page: int = Query(1, ge=1, le=6, title="Esta es la pagina que quieres ver"),
    size: int = Query(0, ge=0, le=9, title="Cuantos registros por página"),
):
    return {"page": page, "size": size}

# Routers image_publication
@app.get("/api/images_publication/{id}", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    image_publication = crudImagePublication.get_by_id(db=db, id=id)
    return image_publication

@app.get("/api/images_publication/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    image_publications = crudImagePublication.get_all(db=db)
    return image_publications

@app.post("/api/images_publication/")
def add(image_publication: schemaImagePublication.ImageInPublicationCreate, db: Session = Depends(get_db)):
    image_publication_result = crudImagePublication.create(image_publication, db)
    return image_publication_result

@app.put("/api/images_publication/")
def update(index: int, image_publication: str, db: Session = Depends(get_db)):
    # publication_list[index] = publication
    # return {"publications": publication_list}
    pass

@app.delete("/api/images_publication/")
def delete(index: int, db: Session = Depends(get_db)):
    # del publication_list[index]
    # return {"publications": publication_list}
    pass

# Routers pets
pet_list = []
@app.get("/api/pets/")
def get():
    return {"pets": pet_list}

@app.post("/api/pets/{pet}")
def add(pet):
    pet_list.append(pet)
    return {"pets": pet_list}

@app.put("/api/pets/")
def update(index: int, pet: str):
    pet_list[index] = pet
    return {"pets": pet_list}

@app.delete("/api/pets/")
def delete(index: int):
    del pet_list[index]
    return {"pets": pet_list}

# Routers publication
@app.get("/api/publications/{id}", status_code=status.HTTP_200_OK)
def get_publication(id: int = Path(...), db: Session = Depends(get_db)):
    publication = crudPublication.get_by_id(db, id)
    return {"publication": publication}


@app.get("/api/publications/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    publications = crudPublication.get_all(db=db)
    return {"publications": publications}
    # return {
    #     "publications": [
    #         Publication.model_validate(publication) for publication in get_all(db=db)
    #     ]
    # }


@app.post("/api/publications/", status_code=status.HTTP_201_CREATED)
def add(
    publication: schemaPublication.Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.crud_create(publication, db)
    return {"publication": publication_result}


@app.put("/api/publications/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int = Path(...),
    publication: schemaPublication.Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crudPublication.crud_update(id, db, publication)
    return {"publication": publication_result}


@app.delete("/api/publications/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int = Path(...), db: Session = Depends(get_db)):
    crudPublication.crud_delete(id, db)

# Routers user
@app.get("/api/users/{id}", status_code=status.HTTP_200_OK)
def get_id(id: int = Path(...), db: Session = Depends(get_db)):
    user = crudUser.get_by_id(db=db, id=id)
    return {"user": user}


@app.get("/api/users/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    users = crudUser.get_all(db=db)
    return {"users": users}


@app.post("/api/users/", status_code=status.HTTP_201_CREATED)
def add(
    user: schemaUser.User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crudUser.crud_create(user, db)
    return {"user": user_result}


@app.put("/api/users/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int = Path(...),
    user: schemaUser.User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crudUser.crud_update(id, db, user)
    return {"user": user_result}


@app.delete("/api/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int = Path(...), db: Session = Depends(get_db)):
    crudUser.crud_delete(id, db)



#app.include_router(router)
#app.include_router(publication_router, prefix="/api/publications")
#app.include_router(user_router, prefix="/api/users")
#app.include_router(image_publication_router, prefix="/api/images_publication")
#app.include_router(pet_router, prefix="/api/pets")
#app.include_router(profile_router, prefix="/api/profiles")
#app.include_router(upload_router, prefix="/api/upload")


# @app.post("/users/", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(
#             status_code=400, detail="El Email ya se encuentra registrado"
#         )
#     return crud_create_user(db=db, user=user)


# @app.get("/users/", response_model=list[User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     return db_user


# @app.get("/publications/{pub_type}", response_model=List[Publication])
# def read_publications(
#     pub_type: PubTypeEnum = Path(
#         ..., title="Publication type", description="Thi is a publication type"
#     ),
#     skip: int = 0,
#     limit: int = 100,
#     db: Session = Depends(get_db),
# ):
#     publications = get_publications_by_pub_type(db, pub_type=pub_type)
#     return publications
