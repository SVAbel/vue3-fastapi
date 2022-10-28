from fastapi import APIRouter

router = APIRouter()

@router.get("/counsel/", tags=["counsel"])
async def get_counsel():
    return "ok"

@router.get("/counsel/{id}", tags=["counsel"])
async def get_counsel(id):
    return id