from pydantic import BaseModel
from typing import List, Optional
from schema.image_publication import ImagesInPublication
from schema.user import User
from schema.pets import Pets
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
    id: int
    publication_date: datetime.date
    pub_type: str
    city: str
    address: Optional[str] = None
    image_publication_id: ImagesInPublication
    # image_publication_id: int
    pet_id: Pets
    user_id: User
    status: PubStatus

    class Config:
        from_attributes = True
        from_orm = True

class PublicationCreate(PublicationBase):
    pass


class Publication(PublicationBase):
    pass

        
