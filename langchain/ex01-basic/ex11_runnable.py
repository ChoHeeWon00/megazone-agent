from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from llm_config import get_llm

def preprocess(d): #전처리
    q = d["question"].strip().lower()
    return {"question" : q}
def postprocess( text ) : #후처리
    text["result"] = f"[답변] {text["result"].strip().upper() }"
    return text
llm = get_llm()

prompt = ChatPromptTemplate([
    ("system","답변은 한문장으로 한다."),
    ("human","{question}")
])| llm | StrOutputParser()

chain = preprocess | RunnableParallel(
    result = prompt , # | llm | StrOutputParser() ,
    original = RunnablePassthrough()
) | postprocess

print( chain.invoke({"question" : "    LLM이 뭐야?   "}))