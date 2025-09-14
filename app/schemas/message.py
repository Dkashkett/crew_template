from pydantic import BaseModel


class MessageRequest(BaseModel):
    user_message: str


class MessageResponse(BaseModel):
    agent_message: str
