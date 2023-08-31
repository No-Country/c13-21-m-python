from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class PetsModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    genre = Column(String, index=True)
    size = Column(String, index=True)
    breed = Column(String, index=True)
    eye_color = Column(String, index=True)
    description = Column(String, index=True)
    fur = Column(String)
    necklace = Column(Boolean)
    color = Column(String)

    # publications= relationship("Publication", back_populates="pet", lazy="joined")
