from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    #SystemMessage()
    ("system","답변은 한줄로 요약한다"),
    ("human","{question}")
])

chain = prompt | llm | StrOutputParser()

res = chain.invoke({"question":"오늘 날씨가 좋아~"})
print( res )
print("--"*20)

res = chain.invoke({"question":"파이썬 설명해줘"})
print( res )


messages = [
    SystemMessage(content="설명"),
]
messages.append(HumanMessage(content="날ㅆㅣ"))
llm.invoke( messages )

messages = [
    SystemMessage(content="설명"),
]
messages.append(HumanMessage(content="파이썬"))
llm.invoke( messages )