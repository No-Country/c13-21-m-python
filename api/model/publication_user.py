from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class PublicationUser(Base):
    __tablename__ = "publications_user"

    publication_user_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    publication_id = Column(Integer, ForeignKey("publications.publication_id"))
