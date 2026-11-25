from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from llm_config import get_llm

llm = get_llm()
parser = CommaSeparatedListOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """너는 목록만 출력하는 도우미야.
     항상 한국어 단어로만, 콤마로 구분해서 답해.
     설명, 인사말, 영어 번역, 접두사(제목)는 절대 붙이지 마."""
    ),
    ("human", "{subject}"),
])
chain = prompt | llm | parser

result = chain.invoke({"subject": input("입력 : ") })
print("--"*20); 
print( result ); 
print("--"*20)
for i, item in enumerate(result, 1):
    print(f"{i}. {item}")
