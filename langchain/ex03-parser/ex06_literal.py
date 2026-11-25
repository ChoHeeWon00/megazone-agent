from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from llm_config import get_llm

class Satisfaction(BaseModel):
    level : Literal["매우 만족", "만족", "보통", "불만", "매우 불만"] = \
                            Field(description="리뷰 문장에 드러난 고객의 만족도")
parser = PydanticOutputParser( pydantic_object = Satisfaction )
print( parser.get_format_instructions() )

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system","""
        너는 고객 리뷰의 만족도를 분류하는 분류기다.
        반드시 아래 형식의 JSON으로만 답한다.
        {format}
    """),
    ("human","{review}")
]).partial( format = parser.get_format_instructions() )

chain = prompt | llm | parser

reviews = [
    "기대 이상이에요! 정말 최고의 제품입니다.",
    "괜찮게 잘 쓰고 있어요",
    "그냥 그래오. 가격 값은 하네요.",
    "배송이 너무 느렸고 품질도 별로에요.",
    "최악입니다. 환불하고 싶어요"
]
result = chain.invoke({"review" : reviews[0]})
print(result )
print("--"*20)
for msg in reviews:
    result = chain.invoke({"review" : msg})
    print(f"[{result.level}] : {msg}")
