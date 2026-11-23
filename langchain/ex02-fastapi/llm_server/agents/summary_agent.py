from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from core.llm import get_llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "다음 리뷰를 한 줄로 요약한다."),
    # 퓨샷 예시
    ("human", "배송이 정말 빠르고 포장도 꼼꼼했어요. 다만 가격이 조금 비싸네요."),
    ("ai", "배송과 포장은 만족스럽지만 가격이 다소 비싸다."),
    ("human", "화면은 선명한데 배터리가 하루도 안 가서 아쉬워요."),
    ("ai", "화면은 선명하나 배터리 지속시간이 짧다."),
    ("human", "맛은 훌륭하지만 양이 적고 매장이 좁아요."),
    ("ai", "맛은 좋지만 양이 적고 매장이 협소하다."),
    # 실제 입력
    ("human", "{text}"),
])
summary_chain = prompt | get_llm() | StrOutputParser()
