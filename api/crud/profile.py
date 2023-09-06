from model.profile import Profile
from schema.profile import Profile as ProfileSchema, ProfileCreate, ProfileUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_by_id(id: int, db:Session):
    profile = db.query(Profile).get(id)

    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return profile


def create(profile: ProfileCreate, db:Session):
    db_profile = Profile(
        name = profile.name,
        phone = profile.phone,
        state = profile.state,
        province = profile.province,
        postal_code = profile.postal_code,
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def update(id: int, db: Session, profile: ProfileUpdate):
    db_profile = get_by_id(id, db)
    if not db_profile:
         raise HTTPException(status_code=404, detail="Profile not found")
    profile_data = profile.dict(exclude_unset=True)
    for key, value in profile_data.items():
         setattr(db_profile, key, value)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
