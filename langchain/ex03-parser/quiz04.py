from typing import Literal
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llm_config import get_llm

class Ticket(BaseModel):
    summary: str = Field(description="문의 내용 요약")
    category: Literal["결제", "배송", "환불", "기타"] = Field(description="문의 분류")
    priority: Literal["높음", "보통", "낮음"] = Field(description="우선순위")
    keywords: list[str] = Field(description="핵심 키워드 목록 (한국어)")

parser = PydanticOutputParser(pydantic_object=Ticket)

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", """너는 문의 메일 자동 분류기야. 메일 본문을 분석해서
                    반드시 아래 형식의 JSON으로만 답해.\n{format}"""),
    ("human", "{email}"),
]).partial(format=parser.get_format_instructions())

chain = prompt | llm | parser
# 여러 예시 입력
emails = [
    "결제는 정상적으로 했는데 상품이 아직도 안 왔어요. 환불해 주세요.",
    "어제 주문한 상품 언제쯤 도착하나요? 빨리 받고 싶어요.",
    "카드 결제가 두 번 됐어요! 당장 처리해 주세요.",
    "단순 변심으로 반품하고 환불받고 싶습니다.",
    "회원 등급은 어떻게 올리나요? 궁금해서 문의드려요.",
]
# 여러 입력을 반복 처리
for i, email in enumerate(emails, 1):
    ticket = chain.invoke({"email": email})
    # 우선순위 높음이면 즉시 처리 문구
    priority_text = ticket.priority
    if ticket.priority == "높음":
        priority_text += " - 즉시 처리"
    print(f"[{i}] {email}")
    print(f"- 분류 : {ticket.category}\n"
          f"- 우선순위: {priority_text}\n"
          f"- 요약: {ticket.summary}\n"
          f"- 키워드: {ticket.keywords}")
    print("-" * 60)
