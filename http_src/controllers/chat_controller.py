from fastapi import APIRouter, status
from http_src.requests.chat.new_msg_request import NewMessageRequest
from services.chatbot import ChatBot
from utils.logger import get_logger

router = APIRouter(
    tags=["chat"],
    prefix="/chat",
)

logger = get_logger()

@router.post("/messages", status_code=status.HTTP_200_OK)
async def send_message(message: NewMessageRequest):
    chatbot = ChatBot()
    response = chatbot.get_response(message.content)
    return response


@router.post("/get_place", status_code=status.HTTP_200_OK)
async def get_place(message: NewMessageRequest):
    chatbot = ChatBot()
    response = chatbot.get_response(message.content)
    return response