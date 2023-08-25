from model.user import User
from schema.user import UserCreate
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def crud_create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.pass_user + "notreallyhashed"
    db_user = User(email=user.email, pass_user=fake_hashed_password, country=user.country)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


