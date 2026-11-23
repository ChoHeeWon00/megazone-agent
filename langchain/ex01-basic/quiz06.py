from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from llm_config import get_llm

llm = get_llm()
sentiment = ChatPromptTemplate.from_messages([
    ("system","다음 리뷰의 감정을 긍정/부정/중립 중 하나로만 답한다. 부연설명은 하지 말아!!"),
    ("human", "배송이 빨라서 좋았어요"),   # 예시 질문
    ("ai", "긍정"),  
    ("human","{text}")]) | llm | StrOutputParser() 
summary   = ChatPromptTemplate.from_messages([
    ("system","다음 리뷰를 한 줄로 요약한다"),
    ("human", "배송은 이틀 만에 왔고 품질도 기대 이상이라 재구매할 생각이에요"),
    ("ai", "빠른 배송과 기대 이상의 품질로 재구매 의사가 있다."),
    ("human","{text}")]) | llm | StrOutputParser() 
keywords  =  ChatPromptTemplate.from_messages([
    ("system","다음 리뷰의 핵심 키워드 3개만 쉼표로 답한다"),
    ("human", "배송은 이틀 만에 왔고 품질도 기대 이상이라 재구매할 생각이에요"),
    ("ai", "배송, 품질, 재구매"),
    ("human","{text}")]) | llm | StrOutputParser() 
chain = RunnableParallel(
    sentiment=sentiment, 
    summary=summary, 
    keywords=keywords, 
    original=RunnablePassthrough(),
) 
out = chain.invoke({"text": "배송은 빨랐지만 포장이 부실했어요"})
print("원문 => ", out["original"])
print("감정 => ", out["sentiment"])
print("요약 => ", out["summary"])
print("키워드 => ", out["keywords"])
