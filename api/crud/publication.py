from sqlalchemy import select
from model.publication import Publication
from schema.publication import (
    PublicationUpdate,
    Publication as PublicationSchema,
    PublicationCreate,
)
from schema.pets import PetCreate
from schema.image_publication import UploadedImage
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from crud import (
    pets as crudPets,
    image_publication as crudImagePublication,
    upload as crudUpload,
)
from model.pets import Pet
from model.image_publication import ImagePublication


def get_by_id(id: int, db: Session):
    # publication = db.query(Publication).get(id)

    # if publication is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return publication

    publication = (
        db.query(Publication)
        .filter(Publication.id == id)
        .options(selectinload(Publication.image_publication))  # Carga la relación image_publication
        .first()
    )

    if publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return publication


def get_sliderPerdidos(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "perdidos")
        .order_by(Publication.publication_date.desc()),
    )


def get_sliderEncontrados(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "encontrados")
        .order_by(Publication.publication_date.desc()),
    )


def get_sliderAdopciones(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "adoptados")
        .order_by(Publication.publication_date.desc()),
    )


def get_viewPerdidos(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "perdidos")
        .order_by(Publication.publication_date.desc()),
    )


def get_viewEncontrados(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "encontrados")
        .order_by(Publication.publication_date.desc()),
    )


def get_viewAdopciones(db: Session):
    return paginate(
        db,
        select(Publication)
        .where(Publication.pub_type == "adoptados")
        .order_by(Publication.publication_date.desc()),
    )


# def get_detailsPublication(id: int, db: Session):
#     publication = db.query(Publication).get(id)

#     if publication is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return publication


# select(Publication).where(Publication.id==id))


def get_all(db: Session):
    return paginate(db, select(Publication))


def create(
    publication: PublicationCreate,
    # pet: PetCreate,
    # image_data: UploadedImage,
    db: Session,
):
    
    print("***esta es antes***")
    print(publication)

    pet_pub = Pet(
        type=publication.pet_publication.type,
        name=publication.pet_publication.name,
        age=publication.pet_publication.age,
        genre=publication.pet_publication.genre,
        size=publication.pet_publication.size,
        breed=publication.pet_publication.breed,
        eye_color=publication.pet_publication.eye_color,
        description=publication.pet_publication.description,
        fur=publication.pet_publication.fur,
        necklace=publication.pet_publication.necklace,
        color=publication.pet_publication.color,
    )

    db_publication = Publication(
        publication_date=publication.publication_date,
        pub_type=publication.pub_type,
        city=publication.city,
        address=publication.address,
        status=publication.status,
        name=publication.name,
        phone=publication.phone,
        pet_publication=pet_pub,
        image_publication=[]
    )


    if isinstance(publication.image_publication, list):
        # Si `image_publication` es una lista, crea objetos ImagePublication y agrégalos a la lista
        for image_data in publication.image_publication:
            pub_image = ImagePublication(image=image_data.image, url=image_data.url)
            db_publication.image_publication.append(pub_image)
    elif publication.image_publication:
        # Si `image_publication` no es una lista pero tiene datos, crea un objeto ImagePublication
        pub_image = ImagePublication(image=publication.image_publication.image, url=publication.image_publication.url)
        db_publication.image_publication.append(pub_image)

    if not db_publication.image_publication:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Missing image information"
        )
    if not db_publication.pet_publication:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Missing pet information"
        )

    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication





def update(id: int, db: Session, publication: PublicationUpdate):
    db_publication = get_by_id(id, db)
    if not db_publication:
        raise HTTPException(status_code=404, detail="Publication not found")
    publication_data = publication.dict(exclude_unset=True)
    for key, value in publication_data.items():
        setattr(db_publication, key, value)
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def delete(id: int, db: Session):
    db_publication = get_by_id(id, db)
    db.delete(db_publication)
    db.commit()
