from enum import Enum
from schema.publication import PubStatus
from config.database import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer, Enum
from sqlalchemy.orm import relationship
from schema.publication import PubTypeEnum, PubStatus

class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(String, index=True)
    pub_type = Column(Enum(PubTypeEnum), index=True)
    city = Column(String(100), index=True)
    address = Column(String(100), index=True)
    status = Column(Enum(PubStatus), index=True)
    name = Column(String(200))
    phone = Column(String(16))
    
    pet_publication = relationship("Pet", back_populates="publication_pet", lazy="joined", uselist=False)
    # image_publication = relationship("ImagePublication", back_populates="publication_image", lazy="joined")
    image_publication = relationship("ImagePublication", back_populates="publication_image")

    # users = relationship("User", secondary="user_publication")
