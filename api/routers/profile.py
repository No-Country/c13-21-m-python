from fastapi import APIRouter, status, HTTPException

profile_router = APIRouter()

profile_list = []


def index_error(index):
    if len(profile_list) <= index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile ID does not exist"
        )


@profile_router.get("/")
def get():
    return {"profiles": profile_list}


@profile_router.post("/", status_code=status.HTTP_201_CREATED)
def add(profile):
    # Verified that index exists
    if profile in profile_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile " + profile.name + " already exist",
        )
    profile_list.append(profile)
    return {"profiles": profile_list}


@profile_router.put("/", status_code=status.HTTP_200_OK)
def update(index: int, profile: str):
    if not index_error(index):
        profile_list[index] = profile
    return {"profiles": profile_list}


@profile_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(index: int):
    if not index_error(index):
        del profile_list[index]
    return {"profiles": profile_list}


# @profile_router.get("/")
# def get():
#     return {"profile": "profile"}
