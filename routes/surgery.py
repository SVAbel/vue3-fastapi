from fastapi import APIRouter

router = APIRouter()

@router.get("/surgery/", tags=["surgery"])
async def get_surgery():
    return "ok"

@router.get("/surgery/{id}", tags=["surgery"])
async def get_surgery(id):
    return id