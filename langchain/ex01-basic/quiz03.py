import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
 
client = ChatBedrockConverse(model=os.getenv("BEDROCK_MODEL_ID"),
                             region_name=os.getenv("AWS_DEFAULT_REGION") )
message = [
    SystemMessage(content="반드시 한국어로 번역해서 답변한다"),
    # ↓ 주석을 풀면 few-shot (단어 하나만 짧게 답하는 형식을 배움)
    HumanMessage(content="run"), 
    AIMessage(content="달리다"),
    HumanMessage(content="beautiful"), 
    AIMessage(content="아름다운"),
]
while True:
    q = input("영어 단어 입력(exit종료) : ")
    if q.lower() == "exit":
        break
    message.append(HumanMessage(content=q))     # 질문 기록
    res = client.invoke(message)
    message.append(res)                          # 답변 기록 → multi-turn
    print(res.content)
    print()