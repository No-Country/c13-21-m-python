from config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    state = Column(String, index=True)
    province = Column(String, index=True)
    postal_code = Column(String, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user_profile = relationship("User", back_populates="profile_user", lazy="joined")
