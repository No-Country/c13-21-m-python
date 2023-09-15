from pydantic import BaseModel
from typing import List, Optional
from schema.user import User, UserDetails
from schema.image_publication import (
    ImageInPublicationCreate,
    ImagesInPublicationCarousel,
    ImagesInPublicationView,
    ImagesInPublicationDetails,
    ImagesInPublication
)
from schema.pets import Pet, PetCarousel, PetView, PetDetails, PetCreate, PetBase
from enum import Enum
import datetime
from pydantic_extra_types.phone_numbers import PhoneNumber


class PubTypeEnum(str, Enum):
    perdidos = "perdidos"
    encontrados = "encontrados"
    adoptados = "adoptados"
    disponibles = "disponibles"


class PubStatus(str, Enum):
    OPEN = "abierta"
    CLOSE = "cerrada"


class PublicationBase(BaseModel):
    publication_date: datetime.date
    pub_type: PubTypeEnum
    city: str
    address: Optional[str] = None
    status: PubStatus
    name: str
    phone: PhoneNumber

    class Config:
        from_attributes = True
        from_orm = True

class PublicationCreate(PublicationBase):
    pet_publication: PetCreate
    image_publication: ImageInPublicationCreate
    
class PublicationInDetail(PublicationBase):
    pass
    # pet_puplication : Pet
    # image_publication : ImagesInPublication

    class Config:
        from_attributes = True
        from_orm = True

class Publication(PublicationBase):
    # id: int
    pet_publication: Pet
    image_publication: List[ImagesInPublication] = []
    # image_publication: ImagesInPublication
    # para la nueva versión
    # user_publication: User

    # class Config:
    #     from_attributes = True
    #     from_orm = True


class PublicationUpdate(BaseModel):
    publication_date: Optional[datetime.date] = None
    pub_type: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    status: Optional[PubStatus] = None


class PublicationCarousel(BaseModel):
    id: int
    publication_date: datetime.date
    city: str
    pet_publication: PetCarousel
    image_publication: List[ImagesInPublicationCarousel] = []


class PublicationView(BaseModel):
    id: int
    publication_date: datetime.date
    address: str
    pet_publication: PetView
    image_publication: List[ImagesInPublicationView] = []


class PublicationDetails(BaseModel):
    id: int
    publication_date: datetime.date
    address: str
    pet_publication: PetDetails
    image_publication: List[ImagesInPublicationDetails] = []
    # user_publication: UserDetails
