from model.user import User
from schema.user import UserCreate, User as UserSchema
from sqlalchemy.orm import Session
from utils.pagination import paginate, PageParams
from fastapi import HTTPException, status


def get_by_id(db: Session, id: int):
    user = db.query(User).get(id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


def get_all(db: Session, skip: int = 0, limit: int = 100):
    users = get_all(db=db)
    return users


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


def pagination(page: int, size: int, db: Session):
    page_params = PageParams()
    # page_params.page = page
    # page_params.size = size
    return paginate(page_params, db.query(User), UserSchema)
