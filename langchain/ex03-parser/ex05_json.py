from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llm_config import get_llm

class Ingredient(BaseModel):
    name : str = Field(description="재료 이름")
    amount : str = Field(description="분량")

class Recipe(BaseModel):
    dish : str = Field(description="요리 이름")
    minutes : int = Field(description="조리 시간(분)")
    ingredient : list[Ingredient] = Field(description="재료 목록")
parser = JsonOutputParser( pydantic_object=Recipe )

prompt = ChatPromptTemplate.from_messages([
    ("system","""
        너는 요리 레시피 도우미야.
        반드시 아래 형식의 JSON으로만 답해.
        {format}
    """),
    ("human","{food} 레시피 알려줘")
]).partial(format=parser.get_format_instructions() )

llm = get_llm()

chain = prompt | llm | parser

r = chain.invoke({"food":"김치볶음밥"})

print( r )
print("--")
print(f"요리 : {r['dish']} / {r['minutes']} 분")
for ing in r['ingredient']:
    print(f"- {ing['name']} : {ing['amount']}")