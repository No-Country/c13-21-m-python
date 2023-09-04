from enum import Enum
from schema.publication import PubStatus
from config.database import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship

class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(String, index=True)
    pub_type = Column(String, index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    status = Column(String, index=True)
    
    pet_publication = relationship("Pet", back_populates="publication_pet", lazy="joined", uselist=False)
    image_publication = relationship("ImagePublication", back_populates="publication_image", lazy="joined")
    user_publication = relationship("User", back_populates="publication_user", lazy="joined", uselist=False)
