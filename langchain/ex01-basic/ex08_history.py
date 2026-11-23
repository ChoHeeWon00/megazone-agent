from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv

from llm_config import get_llm
#load_dotenv()
llm = get_llm()

prompt = ChatPromptTemplate([
    #("system","mess{값}")
    SystemMessage(content="답변은 한줄로 요약한다"),
    MessagesPlaceholder("history"),
    ("human","{q}")
])
h = [
    HumanMessage(content="내 이름은 홍길동이야!"),
    AIMessage(content="반가워요 홍길동님!")
]

input = "내이름 기억해?"
chain = prompt | llm | StrOutputParser()
res = chain.invoke({"q":input, "history":h})
print( res )
