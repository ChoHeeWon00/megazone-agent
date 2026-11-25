from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()
chain = ChatPromptTemplate.from_template(
    "{x}을 한문장으로 설명해"
) | llm | StrOutputParser()

result = chain.invoke({"x":"api"})

print("type : ", type(result) )
print("--"*10)

print("result : ", result )
print("--"*10)

#print("content ", result.content )
#print("--"*10)