from agents.chat_agent import chat_chain
from services.history import history, add_turn

async def get_chat(req : str):
    #stream방식이라 ai msg의 결과를 합처서 하나의 문자열로 저장
    ai_msg = "" 
    async for token in chat_chain.astream( {"input":req, "history":history} ):
            ai_msg += token
            yield token
    add_turn( req, ai_msg) #req(사용자 입력값), ai_msg(llm 응답)   

