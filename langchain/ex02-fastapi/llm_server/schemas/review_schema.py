from pydantic import BaseModel

#요청 값 받기위한 용도
class ReviewReq(BaseModel):
    text : str

#응답 용도
class ReviewRes(BaseModel):
    sentiment : str
    keyword : str
    summary : str
    original : str #dict
