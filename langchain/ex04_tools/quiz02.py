import base64
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field
from pathlib import Path
from llm_config import get_llm

llm = get_llm()

class BusinessCard(BaseModel):
    company:str = Field(description="상호 / 매장명")
    name:str = Field(description="이름")
    phone:str = Field(description="전화번호")
    email:str = Field(description="이메일")
    address:str = Field(description="주소")
class GeneralAnswer(BaseModel):
    origin:str=Field(description="사용자 질문. 원본 내용")
    ai_msg:str=Field(description="사용자 질문에 대한 한 줄 답변")

#CARD_DIR = Path(__file__).parent.parent / "ex03-parser/card"
CARD_DIR = Path(__file__).parents[1] / "ex03-parser/card"

#print( CARD_DIR )

def find_card_file(name:str):
    for ext in ("png", "jpg","jpeg"):
        p = CARD_DIR / f"{name}.{ext}"
        if p.exists():
            return p
    return None

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

card_prompt = ChatPromptTemplate.from_messages([
    ("system","""
        명함에 보이는 모든 글자를 그대로 읽는다.
        읽은 글자를 나열한다.
        설명하지 말고 읽은 텍스트만 출력한다.
    """),
    ("human",[
        {"type": "text",
         "text": "명함의 정보를 추출해줘."},
        {"type":"image", "base64":"{b64}", 
                            "mime_type":"{type}"},
    ])
])

card_chain = card_prompt | llm | StrOutputParser()

@tool
def read_business_card( name : str ):
    """
        저장된 명함 이미지에서 특정 인물의 정보(회사, 직책, 연락처 등)를 찾아 반환한다.
        사용자가 명함 속 특정 사람의 정보를 물어볼 때 사용한다.
    """
    #print("tool args name : ", name)
    img_file = find_card_file(name)
    #print( img_file )
    if img_file is None:
        return f"{name} 명함 파일을 찾을 수 없습니다"

    img_data = img_file.read_bytes()
    #이미지가 .jpg로 됐지만 실제 내부에는 png로 만든 내용일 수 있다. b 확인
    if img_data.startswith(b"\xff\xd8\xff"):
        mime_type = "image/jpeg"
    elif img_data.startswith(b"\x89PNG"):
        mime_type = "image/png"            
    img_b64 = base64.b64encode( img_data ).decode("utf-8")
    # 5. 구조화 출력
    result = card_chain.invoke({"b64":img_b64, "type" : mime_type})
    #print("--- card 정보 result ---")
    #print( result )
    return result

agent = create_agent(
    model= llm,
    tools = [ read_business_card ],
    system_prompt="간략하게 한줄로 설명한다.",
    response_format=BusinessCard | GeneralAnswer
)
def ask( question:str ):
    res = agent.invoke({"messages":[
        #{"role":"user", "content":"내용"}
        #("user","내용")
        HumanMessage(content=question)
    ]})
    return res["structured_response"]

tests = [
   "명함에서 고길동 정보 알려줘" ,
   "명함에서 고고길동 정보 알려줘" ,
   "잘 지내?"
]
for q in tests:
    print("[질문] : ", q)
    answer = ask(q)

    if isinstance( answer, BusinessCard ):
        print("[명함 정보]")
        print("회사 명 : ", answer.company )
        print("이름 : ", answer.name )
    else:
        print("[일반 대화]")
        print(answer.ai_msg)