from fastapi import APIRouter, status
from http_src.requests.chat.new_msg_request import NewMessageRequest

router = APIRouter(
    tags=["chat"],
    prefix="/chat",
)

@router.post("/messages", status_code=status.HTTP_200_OK)
async def send_message(message: NewMessageRequest):
    return {"data": message.content}