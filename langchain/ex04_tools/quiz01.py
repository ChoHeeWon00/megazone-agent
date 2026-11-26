from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
from llm_config import get_llm
from datetime import datetime
@tool
def multiply(a: int, b: int) -> int:
    """두 정수 a와 b를 곱한(곱하기) 값을 반환한다. 곱셈 계산이 필요할 때 사용한다."""
    return a * b
@tool
def now() -> str:
    """현재 시각을 HH:MM 형식으로 반환한다. 지금 몇 시인지 물을 때 사용한다."""
    return datetime.now().strftime("%H:%M")
# 툴 지정(예전 방식)
#tool_map = {"multiply":multiply, "now":now }
#print("tool map : ", tool_map)

# 툴 지정(반복문 활용)
print("툴 이름 확인 -> ", multiply.name )
tools = [ multiply , now ]
tool_map = {t.name: t for t in tools} #dict 형식 툴 등록
print("--"*20)
print("tool map : ", tool_map)



print("=="*20)
llm = get_llm()
llm_tools = llm.bind_tools(tools)

questions = ["3 곱하기 9", "지금 몇 시?", "잘 지내?", ]

for q in questions:
    messages = [
        SystemMessage(content="간략하게 한줄로 설명"),
        HumanMessage(content=q),
    ]
    ai_msg = llm_tools.invoke( messages )
    print(q)
    print(f"content : {ai_msg.content}")
    print(f"tool_calls : {ai_msg.tool_calls}")
    print("--"*20)

    
    if ai_msg.tool_calls:
        messages.append(ai_msg)
        for call in ai_msg.tool_calls:
            result = tool_map[call['name']].invoke(call['args'])
            messages.append(ToolMessage(content=result, tool_call_id=call['id']))
        print(f"content(도구 결과) : {llm.invoke(messages).content}")
    else:
        print(f"content(도구 없는 결과) : {ai_msg.content}")
    print("--"*20)
