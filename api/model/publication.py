from config.database import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Date, Integer, Enum, Boolean
from sqlalchemy.orm import relationship
# from enum import Enum
from schema.publication import PubStatus, PubTypeEnum

class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(Date)
    pub_type = Column(Enum(PubTypeEnum), index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    status = Column(Enum(PubStatus), index=True)
    pet_publication = relationship("Pet", back_populates="publication_pet", lazy="joined")
    image_publication = relationship("ImagePublication", back_populates="publication_image", lazy="joined",)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_publication = relationship("User", back_populates="publication_user", lazy="joined")
