from config.database import get_db
from crud.user import (
    crud_create,
    crud_delete,
    crud_update,
    get_all,
    get_by_id,
    pagination,
)
from fastapi import APIRouter, Body, Depends, Path, status
from schema.user import User
from sqlalchemy.orm import Session

user_router = APIRouter()

user_list = []


@user_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_id(id: int = Path(...), db: Session = Depends(get_db)):
    user = get_by_id(db=db, id=id)
    return {"user": user}


@user_router.get("/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    users = get_all(db=db)
    return {"users": users}


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def add(
    user: User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crud_create(user, db)
    return {"user": user_result}


@user_router.put("/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int = Path(...),
    user: User = Body(...),
    db: Session = Depends(get_db),
):
    user_result = crud_update(id, db, user)
    return {"user": user_result}


@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int = Path(...), db: Session = Depends(get_db)):
    crud_delete(id, db)


# @user_router.get("/")
# def get():
#     return {"user": "user"}
