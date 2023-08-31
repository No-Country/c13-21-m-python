from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from schema.image_publication import ImageInPublicationCreate
from crud.image_publication import get_by_id, get_all, create

image_publication_router = APIRouter()

image_publication_list = []


@image_publication_router.get("/{id}", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    image_publication = get_by_id(db=db, id=id)
    return image_publication

@image_publication_router.get("/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    image_publications = get_all(db=db)
    return image_publications

@image_publication_router.post("/")
def add(image_publication: ImageInPublicationCreate, db: Session = Depends(get_db)):
    image_publication_result = create(image_publication, db)
    return image_publication_result

@image_publication_router.put("/")
def update(index: int, image_publication: str, db: Session = Depends(get_db)):
    # publication_list[index] = publication
    # return {"publications": publication_list}
    pass

@image_publication_router.delete("/")
def delete(index: int, db: Session = Depends(get_db)):
    # del publication_list[index]
    # return {"publications": publication_list}
    pass