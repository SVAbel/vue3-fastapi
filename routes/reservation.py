from fastapi import APIRouter

router = APIRouter()

@router.get("/reservation/", tags=["reservation"])
async def get_reservation():
    return "ok"

@router.get("/reservation/{id}", tags=["reservation"])
async def get_reservation(id):
    return id