from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from enum import Enum


class CountryEnum(str, Enum):
    Mexico = "MX"
    Argentina = "ARG"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    pass_user = Column(String(250))
    country = Column(String)
    is_active = Column(Boolean, default=True)

    profile_user = relationship("Profile", back_populates="user_profile", lazy="joined")
    # publications = relationship("Publication", secondary="user_publication")


class AccessToken(Base):
    __tablename__ = "access_tokens"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    access_token = Column(String(255))
    expiration_date = Column(DateTime(timezone=True))


# user_publication = Table(
#     "user_publication",
#     Base.metadata,
#     Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
#     Column("publication_id", Integer, ForeignKey("publications.id"), primary_key=True),
# )
