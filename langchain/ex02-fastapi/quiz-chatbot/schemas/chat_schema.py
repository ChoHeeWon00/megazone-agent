from pydantic import BaseModel

class ChatReq(BaseModel):
    message: str
