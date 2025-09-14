from fastapi import FastAPI
from app.routes import message

app = FastAPI(title="FastAPI OpenAI Agent App")


app.include_router(message.router, prefix="/api")
