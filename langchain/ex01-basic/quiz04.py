from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm
 
llm = get_llm(temperature=0.5)

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 음식 추천 AI비서다. 답변은 한문장으로 요약한다"),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])
chain = prompt | llm | StrOutputParser()
 
history = []
while True:
    q = input("나(종료-exit) : ")
    if q.lower() == "exit":
        print("--- 프로그램 종료 ---")
        break
    answer = chain.invoke({"question": q, "history": history})
    print("AI 답변 : ", answer)
    
    history.append(HumanMessage(content=q))
    history.append(AIMessage(content=answer))
    
    print("대화 기록 : ", len(history))