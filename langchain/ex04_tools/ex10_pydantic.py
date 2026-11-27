from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from llm_config import get_llm
from tools import multiply

class CalcAnswer(BaseModel):
    """계산 결과"""
    result : int = Field(description="계산 결과 숫자")
    explanin : str = Field(description="계산 과정 한 줄 설명")

agent = create_agent(
    model= get_llm(),
    tools = [multiply],
    system_prompt="간략하게 한 줄로 답한다!!",
    response_format=CalcAnswer
)

res=agent.invoke({"messages":[
                    {"role":"user","content":"3 곱하기 9 곱하기 2"}]})
print( res )
print("--"*20)
print( res["messages"][-1].content )
print("--"*20)
print(res["structured_response"])

print(res["structured_response"].result)
print(res["structured_response"].explanin)
