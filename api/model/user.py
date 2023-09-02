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

    # publications= relationship("Publication")