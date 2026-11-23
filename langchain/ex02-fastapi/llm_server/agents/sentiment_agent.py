from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from core.llm import get_llm

prompt = ChatPromptTemplate([
    ("system","다음 리뷰의 감정을 긍정/부정/중립 중 하나로만 답한다. 부연설명은 하지 말아!!"),
    ("human", "배송이 빨라서 좋았어요"),   # 예시 질문
    ("ai", "긍정"),  
    ("human","{text}")
])

sentiment_chain = prompt | get_llm() | StrOutputParser()