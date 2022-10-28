from fastapi import APIRouter

router = APIRouter()

@router.get("/reception/", tags=["reception"])
async def get_reception():
    return "ok"

@router.get("/reception/{id}", tags=["reception"])
async def get_reception(id):
    return id