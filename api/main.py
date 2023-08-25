from config.database import Base, SessionLocal, engine
from crud.publication import (
   get_publications_by_pub_type
)
from crud.user import get_user, get_user_by_email, get_users, crud_create_user
from fastapi import Depends, FastAPI, HTTPException
from schema.publication import Publication
from schema.user import User, UserCreate
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="El Email ya se encuentra registrado"
        )
    return crud_create_user(db=db, user=user)


@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# @app.get("/publications_by_users/", response_model=list[PublicationsByUser])
# def read_publications_by_users(
#     skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
# ):
#     items = get_publications_by_users(db, skip=skip, limit=limit)
#     return items

# @app.get("/publications/{pub_type}", response_model=Publication)
# def read_publications(pub_type: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     publications = get_publications_by_pub_type(db, pub_type=pub_type)
#     return publications


