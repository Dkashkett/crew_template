from crewai import Flow

from app.config.openai import OpenAIConfig
from app.crews.flow import JokeFlow


class AgentService:
    def __init__(
        self, openai_config: OpenAIConfig = OpenAIConfig(), flow: Flow = JokeFlow()
    ):
        self.config = openai_config
        self.flow = flow

    async def handle_message(self, message: str) -> str:
        return await self.flow.kickoff_async(inputs={"message": message})


def get_agent_service() -> AgentService:
    return AgentService()
