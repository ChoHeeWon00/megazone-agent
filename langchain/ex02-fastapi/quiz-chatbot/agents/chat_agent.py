from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from core.llm import get_llm

SYSTEM_PROMPT = """
당신은 따뜻한 마음을 가진 상담자입니다.

규칙:
- 모든 답변은 반드시 한글로 한다.
- 항상 2-3문장으로 짧게 말한다.
- 공감과 이해를 먼저 표현한다.
- 판단하거나 평가하지 않는다.
- 부드럽고 안정적인 말투를 쓴다.
"""
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder("history"),   # 이전 대화가 들어갈 자리
    ("human", "{input}"),
])
chat_chain = prompt | get_llm() | StrOutputParser()
