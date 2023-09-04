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
    image_publication_id = Column(
        Integer, ForeignKey("image_publication.id"),nullable=False
    )
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(PubStatus), index=True)
    
    pet_publication = relationship("Pet", back_populates="publication_pet", lazy="joined", uselist=False)
    image_publication = relationship("ImagePublication", back_populates="publication_image", lazy="joined")
    user_id = Column(Integer, ForeignKey("users.id"))
    user_publication = relationship("User", back_populates="publication_user", lazy="joined", uselist=False)
