from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from llm_config import get_llm



class Review(BaseModel):
    sentiment : str = Field(description="상/중/하 중 하나")
    score : int = Field(description="1 ~ 5 사이의 값으로 점수 표현")
    keywords : list[str] = Field(description="핵심 키워드")
    content : str = Field(description="입력 값 원본 데이터 저장")

parser = PydanticOutputParser( pydantic_object = Review)
print( parser.get_format_instructions() )

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system","너는 리뷰 분석기야. 반드시 아래 형식의 JSON으로만 답해.\n{test_format}"),
    ("human","{review}")
]).partial(test_format = parser.get_format_instructions() )

chain = prompt | llm | parser

r = chain.invoke(
{"review":"배송은 빨랐지만 포장이 부실해 모서리가 찌그러졌어요. 성능은 만족"})

print(type(r))
print(r)

print("--"*10)
print("감정 : ", r.sentiment)
print("점수 : ", r.score)
print("키워드 : ", r.keywords)
print("원본 : ", r.content)





    