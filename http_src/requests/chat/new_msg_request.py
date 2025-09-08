from pydantic import BaseModel, Field 

class NewMessageRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)
