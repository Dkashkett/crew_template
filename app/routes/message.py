from fastapi import APIRouter, Depends

from app.schemas.message import MessageRequest, MessageResponse
from app.services.agent_service import AgentService, get_agent_service

router = APIRouter()


@router.post("/message", response_model=MessageResponse)
async def handle_message(
    request: MessageRequest, agent_service: AgentService = Depends(get_agent_service)
):
    agent_response = await agent_service.handle_message(request.user_message)
    return MessageResponse(agent_message=agent_response)
