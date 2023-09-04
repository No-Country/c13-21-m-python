from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum


class CountryEnum(str, Enum):
    Mexico = "MX"
    Argentina = "ARG"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    pass_user = Column(String)
    country = Column(String)
    is_active = Column(Boolean, default=True)
    
    publication_id = Column(Integer, ForeignKey("publications.id"))
    publication_user = relationship("Publication", back_populates="user_publication", lazy="joined")
    profile_user = relationship("Profile", back_populates="user_profile", lazy="joined")
    