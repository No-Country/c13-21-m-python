from config.database import Base, SessionLocal, engine
from crud.publication_user import (
    create_publications_by_users,
    get_publications_by_users,
)
from crud.user import get_user, get_user_by_email, get_users
from fastapi import Depends, FastAPI, HTTPException
from schema.publication_user import PublicationsByUser, PublicationsByUserCreate
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
    return create_user(db=db, user=user)


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


@app.post("/users/{user_id}/publications_by_users/", response_model=PublicationsByUser)
def create_publication_for_user(
    user_id: int, publication: PublicationsByUserCreate, db: Session = Depends(get_db)
):
    return create_publications_by_users(db=db, publication=publication, user_id=user_id)


@app.get("/publications_by_users/", response_model=list[PublicationsByUser])
def read_publications_by_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    items = get_publications_by_users(db, skip=skip, limit=limit)
    return items
