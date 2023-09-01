from model.profile import Profile
from schema.profile import Profile as ProfileSchema, PublicationCreate
from sqlalchemy.orm import Session, joinedload
import datetime
from utils.pagination import paginate, PageParams
from fastapi import HTTPException, status


def get_profile_by_id(db:Session, id:int):
    profile = db.query(Profile).get(id)

    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return profile


def profile_create(profile: ProfileSchema, db:Session):
    db_profile = Profile(
        name = profile.name,
        phone = profile.phone,
        state = profile.state,
        province = profile.province,
        postal_code = profile.postal_code,
        user_id = profile.user_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def profile_update(id: int, db: Session, publication: ProfileSchema):
    db_profile = get_profile_by_id(id=id, db=db)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile