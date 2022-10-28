from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/", tags=["dashboard"])
async def get_dashboard():
    return "ok"


@router.get("/dashboard/{id}", tags=["dashboard"])
async def get_dashboard(id):
    return id