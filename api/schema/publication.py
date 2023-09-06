from pydantic import BaseModel
from typing import List, Optional
from schema.user import User, UserDetails
from schema.image_publication import ImagesInPublication, ImagesInPublicationSlider, ImagesInPublicationView, ImagesInPublicationDetails
from schema.pets import Pet, PetSlider, PetView, PetDetails, PetCreate
from enum import Enum
import datetime


class PubTypeEnum(str, Enum):
    perdidos = "Busqueda"
    encontrados = "Encontrada"
    adoptados = "Adoptada"
    disponibles = "En Adopción"


class PubStatus(str, Enum):
    OPEN = "abierta"
    CLOSE = "cerrada"


class PublicationBase(BaseModel):
    publication_date: datetime.date
    pub_type: str
    city: str
    address: Optional[str] = None
    status: PubStatus


class PublicationCreate(PublicationBase):
    pet_publication: PetCreate
    #image_publication: List[ImagesInPublicationCreate] = []


class Publication(PublicationBase):
    id: int
    pet_publication: Pet
    image_publication: List[ImagesInPublication] = []
    user_publication: User

    class Config:
        from_attributes = True
        from_orm = True


class PublicationUpdate(BaseModel):
    publication_date: Optional[datetime.date] = None
    pub_type: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    status: Optional[PubStatus] = None


class PublicationSlider(BaseModel):
    publication_date: datetime.date
    address: str
    pet_publication: PetSlider
    image_publication: List[ImagesInPublicationSlider] = []


class PublicationView(BaseModel):
    publication_date: datetime.date
    address: str
    pet_publication: PetView
    image_publication: List[ImagesInPublicationView] = []


class PublicationDetails(BaseModel):
    publication_date: datetime.date
    address: str
    pet_publication: PetDetails
    image_publication: List[ImagesInPublicationDetails] = []
    user_publication: UserDetails
