from config.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from schema.pets import TypeEnum, GenreEnum, SizeEnum, ColorEnum, FurEnum 

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TypeEnum), index=True)
    name = Column(String(100), index=True)
    age = Column(Integer, index=True)
    genre = Column(Enum(GenreEnum), index=True)
    size = Column(Enum(SizeEnum), index=True)
    breed = Column(String(50), index=True)
    eye_color = Column(Enum(ColorEnum), index=True)
    description = Column(Text(), index=True)
    fur = Column(Enum(FurEnum))
    necklace = Column(Boolean)
    color = Column(Enum(ColorEnum))

    publication_id = Column(Integer, ForeignKey("publications.id"))
    publication_pet = relationship(
        "Publication", back_populates="pet_publication", lazy="joined", uselist=False
    )
