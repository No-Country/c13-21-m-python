from pydantic import BaseModel
from datetime import date
from typing import Optional

class PublicationSchema(BaseModel):
    publication_id: Optional[int]
    date: date
    type: str
    city: str
    address: Optional[str]
    images: list
    pet_id: int
    user_id: int