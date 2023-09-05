from config.database import get_db
from crud.profile import profile_create, profile_update
from fastapi import APIRouter, status, HTTPException
from fastapi import APIRouter, Body, Depends, Path, status
from schema.profile import Profile
from sqlalchemy.orm import Session

profile_router = APIRouter()

profile_list = []


def index_error(index):
    if len(profile_list) <= index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile ID does not exist"
        )


@profile_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_profile_by_id(
    id: int = Path(...),
    db: Session = Depends(get_db)
    ):
    profile = get_profile_by_id(db, id)
    return {"profile": profile}


#@profile_router.get("/")
#def get():
#    return {"profiles": profile_list}


@profile_router.post("/", status_code=status.HTTP_201_CREATED)
def add(
    profile: Profile = Body(...),
    db: Session = Depends(get_db),
    ):
    profile_result = profile_create(profile, db)
    return {"profile": profile_result}

    # Verified that index exists
    #if profile in profile_list:
    #    raise HTTPException(
    #        status_code=status.HTTP_400_BAD_REQUEST,
    #        detail="Profile " + profile.name + " already exist",
    #    )
    #profile_list.append(profile)
    #return {"profiles": profile_list}


@profile_router.put("/{id}", status_code=status.HTTP_200_OK)
def update(
    id: int = Path(...),
    profile: Profile = Body(...),
    db: Session = Depends(get_db),
    ):
    profile_result = profile_update(id, db, profile)
    return {"profile": profile_result}
    #if not index_error(index):
    #    profile_list[index] = profile
    #return {"profiles": profile_list}


#@profile_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
#def delete(index: int):
#    if not index_error(index):
#        del profile_list[index]
#    return {"profiles": profile_list}


# @profile_router.get("/")
# def get():
#     return {"profile": "profile"}
