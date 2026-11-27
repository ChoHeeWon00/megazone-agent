from langchain.agents import create_agent
from llm_config import get_llm
from tools import multiply

agent = create_agent(
    model = get_llm(),
    tools=[ multiply ],
    system_prompt="간략하게 한 줄로 답한다!!"
)

res = agent.invoke(
    {"messages":[
            {"role":"user", "content":"3 곱하기 9 곱하기 2"}
        ]
    }
)
print( res )
for t in res["messages"]:
    print( type(t) )
print("=="*10)
print( res["messages"][-1] )
print("=="*10)
print( res["messages"][-1].content )

from langchain_core.output_parsers import StrOutputParser
chain = (
    #agent | (lambda ai_msg: ai_msg["messages"][-1].content)
    agent | (lambda ai_msg: ai_msg["messages"][-1]) | StrOutputParser()
)
res = chain.invoke(
    {"messages":[
            {"role":"user", "content":"3 곱하기 9 곱하기 2"}
        ]
    }
)
print("--- res ---")
print( res )