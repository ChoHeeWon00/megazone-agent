from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from llm_config import get_llm
from tools import multiply

class CalcAnswer(BaseModel):
    """계산 결과"""
    result : int = Field(description="계산 결과 숫자")
    explanin : str = Field(description="계산 과정 한 줄 설명")

class GeneralAnswer(BaseModel):
    """계산이 필요 없는 일반 질문에 대한 답변을 한다"""
    origin:str=Field(description="사용자 질문. 원본 내용")
    ai_msg:str=Field(description="사용자 질문에 대한 한 줄 답변")

agent = create_agent(
    model=get_llm(),
    tools = [multiply],
    system_prompt="간략하게 한 줄로 답변한다.",
    response_format = CalcAnswer | GeneralAnswer
)

messages = ["3 곱하기 9","잘 지내?", "3 곱하기 9 곱하기 2"]
"""
res = agent.invoke({"messages" : 
                    [{"role":"user", "content":messages[0]}]})
print( res["structured_response"] )
print("--"*20)
res = agent.invoke({"messages" : 
                    [{"role":"user", "content":messages[1]}]})
print( res["structured_response"] )
"""
def ask( question : str):
    res = agent.invoke({"messages" : 
                    [{"role":"user", "content":question}]})
    #print( type(res["structured_response"]) )
    return res["structured_response"]
#ask( messages[0] )
#ask( messages[1] )

for q in messages:
    answer = ask(q)
    if isinstance(answer, CalcAnswer):
        print("[계산 결과]")
        print( answer ) # answer.result, answer.explanin
    elif isinstance(answer, GeneralAnswer):
        print("[일반 대화]")
        print( answer )# answer.origin, answer.ai_msg