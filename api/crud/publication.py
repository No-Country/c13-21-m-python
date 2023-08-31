from model.publication import Publication
from schema.publication import Publication as PublicationSchema, PublicationCreate
from sqlalchemy.orm import Session, joinedload
from schema.image_publication import ImagesInPublication
import datetime
from utils.pagination import paginate, PageParams
from fastapi import HTTPException, status


# def get_publications_by_pub_type(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(PublicationUser).offset(skip).limit(limit).all()

def get_by_id(db:Session, id:int):
    publication = db.query(Publication).get(id)

    if publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return publication

def get_all(db:Session):
    publications = db.query(Publication).all()
    return publications

def crud_create(publication: PublicationSchema, db:Session):
    db_publication = Publication(
        publication_date = publication.date,
        pub_type = publication.pub_type,
        city = publication.city,
        address = publication.address,
        image_publication_id = publication.image_publication_id,
        pet_id = publication.pet_id,
        user_id = publication.user_id,
        status = publication.status
    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication

def crud_update(id: int, db: Session, publication: PublicationSchema):
    db_publication = get_by_id(id=id, db=db)
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication

def crud_delete(id: int, db: Session):
    db_publication = get_by_id(id=id, db=db)
    db.delete(db_publication)
    db.commit()

def pagination(page: int, size: int, db:Session):
    page_params = PageParams()
    # page_params.page = page
    # page_params.size = size
    return paginate(page_params, db.query(Publication), PublicationSchema)

# def get_publications_by_pub_type(db: Session, pub_type: str):
#     publications = (
#         db.query(Publication)
#         .filter(Publication.pub_type == pub_type)
#         .options(joinedload(Publication.image))
#         .all()
#     )

#     result = []
#     for publication in publications:
#         images = [
#             ImagesInPublication(id=image.id, image=image.image, url=image.url)
#             for image in publication.image
#         ]
#         publication_data = PublicationSchema(
#             **publication.__dict__,
#             image_publication_id=images
#         )
#         result.append(publication_data)

#     return result

    # images = db.query(ImagePublication).filter(ImagePublication.image_publication_id == Publication.image_publication_id).all()
    # publications_with_images["image_publication_id"] = images
    # return publications_with_images

# def create_publications_by_users(
#     db: Session, publication: PublicationsByUserCreate, user_id: int
# ):
#     db_publication_by_user = PublicationUser(**publication.dict(), owner_id=user_id)
#     db.add(db_publication_by_user)
#     db.commit()
#     db.refresh(db_publication_by_user)
#     return db_publication_by_user
