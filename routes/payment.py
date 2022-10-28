from fastapi import APIRouter

router = APIRouter()

@router.get("/payment/", tags=["payment"])
async def get_payment():
    return "ok"

@router.get("/payment/{id}", tags=["payment"])
async def get_payment(id):
    return id