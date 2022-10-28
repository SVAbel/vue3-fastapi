from fastapi import APIRouter

router = APIRouter()

@router.get("/bom/", tags=["bom"])
async def get_bom():
    return "ok"

@router.get("/bom/{id}", tags=["bom"])
async def get_bom(id):
    return id