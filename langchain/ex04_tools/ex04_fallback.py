#BEDROCK_MODEL_ID2=apac.amazon.nova-lite-v1:0
#BEDROCK_MODEL_FAIL=apac.amazon.nova-note-exist-v1:0

from langchain_core.messages import HumanMessage
from llm_config import get_llm

primary = get_llm(model="BEDROCK_MODEL_FAIL")
backup = get_llm(model="BEDROCK_MODEL_ID2")

robust = primary.with_fallbacks( [backup] )

res = robust.invoke([HumanMessage(content="안녕")])
print("모델 확인 : ", res.response_metadata["model_name"])
print(res.content)