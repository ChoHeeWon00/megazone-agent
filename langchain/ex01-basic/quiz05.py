from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from llm_config import get_llm

def preprocess(d): #전처리
    q = d["question"].strip().lower()
    return {"question" : q}
def postprocess( text ) : #후처리
    return f"[답변] {text.strip().upper() }"

print("-- 전처리 --")
chain = RunnableLambda( preprocess )
print( chain.invoke({"question":"    LLM이 뭐야?   "}))

print("-- 후처리 --")
chain = RunnableLambda( postprocess )
print( chain.invoke("    llm이 뭐야?   "))

print()
print("--- 최종 답변 ---")

llm = get_llm()

prompt = ChatPromptTemplate([
    ("system","답변은 한문장으로 작성한다"),
    ("human","{question}")
])
# {"question" : q}
chain = preprocess  | prompt | llm | StrOutputParser() | postprocess
print(chain.invoke({"question" : "llm이 뭐야?"}))


