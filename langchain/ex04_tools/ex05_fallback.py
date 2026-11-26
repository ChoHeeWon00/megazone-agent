from langchain_core.messages import HumanMessage
from llm_config import get_llm
from langchain_core.prompts import ChatPromptTemplate

primary = get_llm(model="BEDROCK_MODEL_FAIL") # get_llm(model="BEDROCK_MODEL_FAIL")
backup = get_llm(model="BEDROCK_MODEL_ID2")

prompt = ChatPromptTemplate.from_messages([
    ("system","답변은 간략하게 한줄로 말한다"),
    ("human","{q}")
])

primary_chain = prompt | primary
backup_chain = prompt | backup

robust_chain = primary_chain.with_fallbacks([backup_chain])
res = robust_chain.invoke({"q":"안녕"})

print("모델 명 : ", res.response_metadata["model_name"])
print( res.content )