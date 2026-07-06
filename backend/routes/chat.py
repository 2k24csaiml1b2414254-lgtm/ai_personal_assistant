from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.groq_service import ask_groq

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = ask_groq(
            system_prompt="You are a helpful AI personal assistant.",
            user_prompt=request.message
        )

        return ChatResponse(response=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )