from fastapi import APIRouter

router = APIRouter()

@router.get("/calendar/", tags=["calendar"])
async def get_calendar():
    return "ok"

@router.get("/calendar/{id}", tags=["calendar"])
async def get_calendar(id):
    return id