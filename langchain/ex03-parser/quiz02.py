from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llm_config import get_llm

class Card(BaseModel):
    name: str = Field(description="사람의 이름")
    company: str = Field(description="회사명")
    phone: str = Field(description="전화번호 (예: 010-1234-5678)")
    email: str = Field(description="이메일 주소")
parser = PydanticOutputParser(pydantic_object=Card) # Card 형식으로 변환할 parser 생성

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 명함 정보 추출기야. 명함 문장에서 정보를 뽑아 반드시 아래 형식의 JSON으로만 답해.\n{format_instructions}"),
    ("human", "{business_card}"),
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser
# 명함 문장에서 추출
card = chain.invoke({"business_card":"홍길동 남성 ABC컴퍼니 마케팅팀 010-1234-5678 kim@abc.com"})
# card.email 처럼 필드를 직접 출력
print(f"이름: {card.name}\n회사: {card.company}\n전화: {card.phone}\n이메일: {card.email}")
