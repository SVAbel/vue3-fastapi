from fastapi import APIRouter

router = APIRouter()

@router.get("/van/", tags=["van"])
async def get_van():
    return "ok"

@router.get("/van/{id}", tags=["van"])
async def get_van(id):
    return id