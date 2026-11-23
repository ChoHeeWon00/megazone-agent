from langchain_core.runnables import RunnablePassthrough, RunnableLambda

chain = RunnablePassthrough()

print( chain.invoke("안녕") )
print( chain.invoke({"aaa":111}) )
print( chain.invoke([1,2,3,4,54]) )

def clean(d): #d = {"text":"내용"}
    return {"text":d["text"].lower() }

#print( clean({"text":"LangChain"}) )

chain = RunnableLambda( clean )
print( chain.invoke({"text":"LangChain"}) )

chain = clean | RunnablePassthrough()
print( chain.invoke({"text":"LangChain"}) )
