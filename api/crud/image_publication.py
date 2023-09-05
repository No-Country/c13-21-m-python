from model.image_publication import ImagePublication
from schema.image_publication import ImageInPublicationCreate, ImageInPublicationUpdate
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def get_by_id(id:int, db:Session):
    image_publication = db.query(ImagePublication).get(id)

    if image_publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return image_publication


def create(image: ImageInPublicationCreate):
    db_image_publication = ImagePublication(
        image = image.image,
        url = image.url
        )
    return db_image_publication


def update(image: ImageInPublicationUpdate):
    db_image_publication = ImagePublication(
        image = image.image,
        url = image.url
        )
    return db_image_publication


def update(id: int, db: Session, image_publication: ImageInPublicationUpdate):
    db_image_publication = get_by_id(id, db)
    if not db_image_publication:
         raise HTTPException(status_code=404, detail="Image not found")
    image_publication_data = image_publication.dict(exclude_unset=True)
    for key, value in image_publication_data.items():
         setattr(db_image_publication, key, value)
    db.add(db_image_publication)
    db.commit()
    db.refresh(db_image_publication)
    return db_image_publication
