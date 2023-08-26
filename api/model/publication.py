from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum

class PubTypeEnum(str, Enum):
    perdidos = "Busqueda"
    encontrados = "Encontrada"
    adoptados = "Adoptada"

class Publication(Base):
    __tablename__ = "publications"

    publication_id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(Date)
    pub_type = Column(String, index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    image_publication_id = Column(
        Integer, ForeignKey("image_publication_id")
    )
    pet_id = Column(Integer, ForeignKey("pets.pet_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
