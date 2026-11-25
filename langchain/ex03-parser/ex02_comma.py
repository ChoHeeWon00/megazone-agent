from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser

from llm_config import get_llm

llm = get_llm()

parser = CommaSeparatedListOutputParser() #StrOutputParser()

prompt = ChatPromptTemplate.from_template("{x} 콤마로 구분해 나열해줘")
chain = prompt | llm | parser
result = chain.invoke({"x":"파이썬 자료형 알려줘"})

print( type(result) )
print( result )
print( result[0] )