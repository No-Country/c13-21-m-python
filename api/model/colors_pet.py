from config.database import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ColorsPet(Base):
    __tablename__ = "colors_pet"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String)
