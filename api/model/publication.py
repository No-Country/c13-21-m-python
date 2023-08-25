from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Publication(Base):
    __tablename__ = "publications"

    publication_id = Column(Integer, primary_key=True, index=True)
    publication_date = Column(Date)
    pub_type = Column(String, index=True)
    city = Column(String, index=True)
    address = Column(String, index=True)
    image_publication_id = Column(
        Integer, ForeignKey("image_publication_id")
    )
    pet_id = Column(Integer, ForeignKey("pets.pet_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))

    # publications_by_user = relationship(
    #     "User", back_populates="users_with_publication"
    # )
    # images = relationship("ImagePublication")
    # pets = relationship("Pets")

    users= relationship("User")