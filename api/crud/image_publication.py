from model.image_publication import ImagePublication
from schema.publication import Publication as PublicationSchema, PublicationCreate
from schema.image_publication import ImageInPublicationCreate
from sqlalchemy.orm import Session, joinedload
from schema.image_publication import ImagesInPublication
import datetime

# def get_publications_by_pub_type(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(PublicationUser).offset(skip).limit(limit).all()

def get_by_id(db:Session, id:int):
    publication = db.query(ImagePublication).get(id)
    return publication

def get_all(db:Session):
    publications = db.query(ImagePublication).all()
    return publications

def create(image_publication: ImageInPublicationCreate, db:Session):
    image_publication_db = ImagePublication(
        # publication_date = datetime.date.isoformat(publication.publication_date)
        image = image_publication.image,
        url = image_publication.url,
    )
    db.add(image_publication_db)




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
