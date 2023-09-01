from main import get_db
from crud.publication import crud_create, crud_delete, crud_update, get_all, get_by_id
from fastapi import APIRouter, Body, Depends, Path, status
from schema.publication import Publication
from sqlalchemy.orm import Session

publication_router = APIRouter()

publication_list = []


@publication_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_publication(id: int = Path(...), db: Session = Depends(get_db)):
    publication = get_by_id(db, id)
    return {"publication": publication}


@publication_router.get("/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    publications = get_all(db=db)
    return {"publications": publications}
    # return {
    #     "publications": [
    #         Publication.model_validate(publication) for publication in get_all(db=db)
    #     ]
    # }


@publication_router.post("/", status_code=status.HTTP_201_CREATED)
def add(
    publication: Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crud_create(publication, db)
    return {"publication": publication_result}


@publication_router.put("/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int = Path(...),
    publication: Publication = Body(...),
    db: Session = Depends(get_db),
):
    publication_result = crud_update(id, db, publication)
    return {"publication": publication_result}


@publication_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int = Path(...), db: Session = Depends(get_db)):
    crud_delete(id, db)
