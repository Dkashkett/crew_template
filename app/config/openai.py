from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env.local")


class OpenAIConfig(BaseSettings):
    openai_api_key: str


# Create a single instance to use across the app
OPENAI_CONFIG = OpenAIConfig()
