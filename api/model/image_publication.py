from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ImagePublication(Base):
    __tablename__ = "image_publication"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    url = Column(String)

    publications = relationship("Publication", back_populates="image", lazy="joined")