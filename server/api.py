from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.assistant import Assistant

app = FastAPI(title="V.E.I.D.A. Core", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatIn(BaseModel):
    message: str


@app.post("/api/chat")
async def chat(body: ChatIn):
    assistant = Assistant()
    reply = await assistant.respond(body.message)
    return {"reply": reply}


@app.get("/api/status")
def status():
    return {"status": "online", "version": "0.1.0"}
