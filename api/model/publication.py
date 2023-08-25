from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Publication(Base):
    __tablename__ = "publications"

    publication_id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    type = Column(String, index=True)
    country = Column(String, index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    images_publication_id = Column(
        Integer, ForeignKey("images_publication.images_publication_id")
    )
    pet_id = Column(Integer, ForeignKey("pets.pet_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))

    images = relationship("ImagePublication", back_populates="image_with_publications")
    publications_by_user = relationship(
        "PublicationUser", back_populates="users_with_publication"
    )
    pets = relationship("Pets", back_populates="pets_with_publication")
