from fastapi import APIRouter

router = APIRouter(
    tags=["chat"],
    prefix="/chat",
)

@router.post("/messages")
async def send_message(message: str):
    return {"data": message}