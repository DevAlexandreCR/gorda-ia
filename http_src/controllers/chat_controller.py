from fastapi import APIRouter, status

router = APIRouter(
    tags=["chat"],
    prefix="/chat",
)

@router.post("/messages", status_code=status.HTTP_200_OK)
async def send_message(message: str):
    return {"data": message}