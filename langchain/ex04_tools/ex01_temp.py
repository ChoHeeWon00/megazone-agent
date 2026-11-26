from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage

from llm_config import get_llm

fact_llm = get_llm(temperature=0.0)
idea_llm = get_llm(temperature=1.0)

sysMsg = SystemMessage( content="답변은 한줄로 요약한다.")
prompt = ChatPromptTemplate.from_messages([
    sysMsg, HumanMessage(content="카페 이름 3개 제안")
])
parser = StrOutputParser()

fact_chain = prompt | fact_llm | parser

print(f"[사실] : {fact_chain.invoke({})}")
print()

idea_chain = prompt | idea_llm | parser

print(f"[사실] : {idea_chain.invoke({})}")
print()