from model.publication import Publication
from model.user import User
from schema.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_by_id(id:int, db: Session):
    user = db.query(User).get(id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_all(db: Session, skip: int = 0, limit: int = 100):
    users = get_all(db)
    return users


def get_publications(id:int, db:Session):
    publications = db.query(Publication).filter(Publication.user_publication.has(User.id == id)).all()

    if publications is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return publications


def create(user: UserCreate, db: Session):
    fake_hashed_password = user.pass_user + "notreallyhashed"
    db_user = User(
        email=user.email, pass_user=fake_hashed_password, country=user.country
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(id: int, db: Session, user: UserUpdate):
    db_user = get_by_id(id, db)
    if not db_user:
         raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
         setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete(id: int, db: Session):
    db_user = get_by_id(id, db)
    db.delete(db_user)
    db.commit()
