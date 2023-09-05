from model.publication import Publication
from model.user import User
from schema.user import UserCreate, User as UserSchema
from sqlalchemy.orm import Session
from utils.pagination import paginate, PageParams
from fastapi import HTTPException, status


def get_by_id(id:int, db: Session):
    user = db.query(User).get(id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_all(db: Session, skip: int = 0, limit: int = 100):
    users = get_all(db=db)
    return users


def get_publications(id:int, db:Session):
    publications = db.query(Publication).filter(Publication.user_publication.has(User.id == id)).all()

    if publications is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return publications


def crud_create(db: Session, user: UserCreate):
    fake_hashed_password = user.pass_user + "notreallyhashed"
    db_user = User(
        email=user.email, pass_user=fake_hashed_password, country=user.country
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def crud_update(id: int, db: Session, user: UserCreate):
    db_user = get_by_id(id=id, db=db)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def crud_delete(id: int, db: Session):
    db_user = get_by_id(id=id, db=db)
    db.delete(db_user)
    db.commit()
