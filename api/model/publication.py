from config.database import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Date, Integer, Enum, Boolean
from sqlalchemy.orm import relationship
# from enum import Enum
from model.image_publication import ImagePublication
from schema.publication import PubStatus, PubTypeEnum



class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(Date)
    pub_type = Column(Enum(PubTypeEnum), index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    image_publication_id = Column(
        Integer, ForeignKey("image_publication.id"),nullable=False
    )
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(PubStatus), index=True)


    image = relationship("ImagePublication", lazy="joined", back_populates="publications")
    # pet = relationship("PetsModel", lazy="joined", back_populates="publications")
    user = relationship("User", lazy="joined")

    # pet_publication = relationship("Pets")
    # user_publication = relationship("User")