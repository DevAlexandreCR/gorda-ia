from pydantic import BaseModel, Field
from constants.session_status import SessionStatus

class NewMessageRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000, example="Hola, necesito un servicio.")
    session_status: SessionStatus = Field(..., description="Current status of the user session")
