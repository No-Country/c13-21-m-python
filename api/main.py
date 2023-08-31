from config.database import Base, SessionLocal, engine
# from crud.publication import get_publications_by_pub_type
# from crud.user import get_user, get_user_by_email, get_users, crud_create_user
from fastapi import Depends, FastAPI, HTTPException, Query, Path, APIRouter
from schema.publication import Publication
from schema.user import User, UserCreate
from sqlalchemy.orm import Session
from model.publication import PubTypeEnum
from typing import List, Dict, Any, Optional
from routers.publication import publication_router
from routers.user import user_router
from routers.image_publication import image_publication_router
from routers.pet import pet_router
from routers.profile import profile_router
from routers.upload import upload_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()





@app.get("/e_page")
def page(
    page: int = Query(1, ge=1, le=6, title="Esta es la pagina que quieres ver"),
    size: int = Query(0, ge=0, le=9, title="Cuantos registros por página"),
):
    return {"page": page, "size": size}


app.include_router(router)
app.include_router(publication_router, prefix="/api/publications")
app.include_router(user_router, prefix="/api/users")
app.include_router(image_publication_router, prefix="/api/images_publication")
app.include_router(pet_router, prefix="/api/pets")
app.include_router(profile_router, prefix="/api/profiles")
app.include_router(upload_router, prefix="/api/upload")


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
