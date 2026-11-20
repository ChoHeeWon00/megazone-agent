import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

messages = [
    SystemMessage(content="답변은 한줄로 간략하게 작성한다"), 
    HumanMessage(content="내 이름은 홍길동이야!")
]
res = llm.invoke( messages )
print( res.content )
print("--"*20)

messages = [
    SystemMessage(content="답변은 한줄로 간략하게 작성한다"),
    HumanMessage(content="내 이름은 홍길동이야!"),
    AIMessage(content=res.content),  #res, 
    HumanMessage(content="내 이름 기억해?")
]
res = llm.invoke( messages )
print( res.content )

print("--"*20)

print( type(res) )
print( res )

