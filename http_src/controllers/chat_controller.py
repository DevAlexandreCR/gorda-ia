from fastapi import APIRouter, status
from http_src.requests.chat.new_msg_request import NewMessageRequest
from services.chatbot import ChatBot

router = APIRouter(
    tags=["chat"],
    prefix="/chat",
)

@router.post("/messages", status_code=status.HTTP_200_OK)
async def send_message(message: NewMessageRequest):
    chatbot = ChatBot()
    response = chatbot.get_response(message.content)
    return {"data": response}

@router.post("/get_place", status_code=status.HTTP_200_OK)
async def get_place(message: NewMessageRequest):
    chatbot = ChatBot()
    response = chatbot.get_response(message.content)
    return {"data": response}