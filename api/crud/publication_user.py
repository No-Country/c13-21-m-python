from model.publication_user import PublicationUser
from schema.publication_user import PublicationsByUserCreate
from sqlalchemy.orm import Session


def get_publications_by_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PublicationUser).offset(skip).limit(limit).all()


def create_publications_by_users(
    db: Session, publication: PublicationsByUserCreate, user_id: int
):
    db_publication_by_user = PublicationUser(**publication.dict(), owner_id=user_id)
    db.add(db_publication_by_user)
    db.commit()
    db.refresh(db_publication_by_user)
    return db_publication_by_user
