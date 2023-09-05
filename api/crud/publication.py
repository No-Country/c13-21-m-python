from sqlalchemy import select
from model.publication import Publication
from schema.publication import PublicationUpdate, Publication as PublicationSchema, PublicationCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate


def get_by_id(db:Session, id:int):
    publication = db.query(Publication).get(id)

    if publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return publication


def get_sliderPerdidos(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="perdidos").order_by(Publication.publication_date.desc()))


def get_sliderEncontrados(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="encontrados").order_by(Publication.publication_date.desc()))


def get_sliderAdopciones(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="adoptados").order_by(Publication.publication_date.desc()))


def get_viewPerdidos(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="perdidos").order_by(Publication.publication_date.desc()))


def get_viewEncontrados(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="encontrados").order_by(Publication.publication_date.desc()))


def get_viewAdopciones(db: Session):
    return paginate(db, select(Publication).where(Publication.pub_type=="adoptados").order_by(Publication.publication_date.desc()))


# def get_detailsPublication(id: int, db: Session):
#     publication = db.query(Publication).get(id)

#     if publication is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return publication


# select(Publication).where(Publication.id==id))


def get_all(db:Session):
    return paginate(db, select(Publication))


def create(publication: PublicationCreate, db:Session):
    db_publication = Publication(
        publication_date = publication.date,
        pub_type = publication.pub_type,
        city = publication.city,
        address = publication.address,
        status = publication.status,
    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def update(
        id: int,
        db: Session,
        publication: PublicationUpdate
        ):
    db_publication = get_by_id(id, db)
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def delete(id: int, db: Session):
    db_publication = get_by_id(id, db)
    db.delete(db_publication)
    db.commit()
