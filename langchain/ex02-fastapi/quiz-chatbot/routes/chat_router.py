from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.chat_service import get_chat
from schemas.chat_schema import ChatReq

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/stream")
async def chat_stream(req : ChatReq):
    return StreamingResponse(get_chat(req.message), media_type="text/plain; charset=utf-8")
