from agents.chat_agent import chat_chain
from services.history import history, add_turn, get_history

async def get_chat(req : str, username:str):
    h = get_history(username)
    #stream방식이라 ai msg의 결과를 합처서 하나의 문자열로 저장
    ai_msg = "" 
    async for token in chat_chain.astream( 
                        {"input":req, "history":h} ):
            ai_msg += token 
            yield token
    add_turn(username, req, ai_msg) #req(사용자 입력값), ai_msg(llm 응답)   
