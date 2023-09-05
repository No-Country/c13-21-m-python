from config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.publication import Publication


class ImagePublication(Base):
    __tablename__ = "image_publication"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    url = Column(String, index=True)

    publication_id = Column(Integer, ForeignKey("publications.id"))
    publication_image = relationship(Publication, back_populates="image_publication", lazy="joined")
