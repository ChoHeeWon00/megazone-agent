import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from llm_config import get_llm

llm_01 = get_llm(temperature=0.0)

prompt_01 = ChatPromptTemplate([
    ("system","반말로 답변한다."),
    ("human","{text01}")
])

chain_01 = prompt_01 | llm_01 | StrOutputParser()

start = time.time()
print( chain_01.invoke({"text01":"안녕"}))
print("--"*10)

llm_02 = get_llm(temperature=0.9)

prompt_02 = ChatPromptTemplate([
    ("system","친절하게 답변한다."),
    ("human","{text02}")
])

chain_02 = prompt_02 | llm_02 | StrOutputParser()

end = time.time() - start
print( chain_02.invoke({"text02":"안녕"}))
print(f"실행 시간 : {end:.3f} 초")

print("--"*10)

chain = RunnableParallel(
    user_key01 = chain_01,
    user_key02 = chain_02
)

start = time.time()
answer = chain.invoke({"text01":"안녕", "text02":"안녕"})
print( answer )

end = time.time() - start
print("걸린 시간 : ", end)
print( answer["user_key01"] )

