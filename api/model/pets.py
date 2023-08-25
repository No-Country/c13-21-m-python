from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Pets(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    genre = Column(String, index=True)
    size = Column(String, index=True)
    breed = Column(String, index=True)
    eye_color = Column(String, index=True)
    distinctive_feature = Column(String, index=True)
    colors_pet_id = Column(Integer, ForeignKey("colors_pet.colors_pet_id"))
    pubication_id = Column(Integer, ForeignKey("publications.publication_id"))

    colors = relationship("ColorsPet", back_populates="pets_with_colors")
