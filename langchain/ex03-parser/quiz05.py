import base64
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from pathlib import Path

from llm_config import get_llm

# 1. 명함에서 뽑을 구조 정의
class BusinessCard(BaseModel):
    company: str = Field(description="상호 / 매장명")
    name: str = Field(description="이름")
    phone: str = Field(description="전화번호")
    email: str = Field(description="이메일")
    address: str = Field(description="주소")
# 2. 이미지 + 지시(형식 안내 포함) 생성
prompt = ChatPromptTemplate.from_messages([
    ("system","명함 이미지에서 정보를 추출해줘."),
    ("human",[
        {"type": "text",
         "text": "정보를 추출해줘."},
        {"type":"image", "base64":"{b64}", "mime_type":"{type}"},
    ])
])
# 3. 비전 모델
llm = get_llm()
img_file = Path(__file__).parent / "card" 
while True:
    name = input("확인할 사용자 이름 입력 : ")
    matches = list(img_file.glob(f"{name}.*")) #확장자 관계없이 파일 찾기
    print(matches) # 파일이 있으면 [ 홍길동.확장자 ] 
    #img_path = matches[0]
    #print( img_path.name ) #파일명만 가져옴 홍길동.jpg
    #print( img_path.stem ) # 확장자 없이 이름만(홍길동)
    #print( img_path.suffix ) # 확장자만 가져옴 .jpg
    if matches:
        img_path = matches[0]
        mime_type = img_path.suffix
        # byte형식으로 실제 확장자 확인
        #p = Path(__file__).parent / "card" / "홍길동.jpg"
        #print(p.read_bytes()[:8])  
        if mime_type in [".png", ".jpg",".jpeg"]:
            img_data = img_path.read_bytes()
            #이미지가 .jpg로 됐지만 실제 내부에는 png로 만든 내용일 수 있다. b 확인
            if img_data.startswith(b"\xff\xd8\xff"):
                mime_type = "image/jpeg"
            elif img_data.startswith(b"\x89PNG"):
                mime_type = "image/png"            
            img_b64 = base64.b64encode( img_data ).decode("utf-8")
            # 5. 구조화 출력
            llm_structured = prompt | llm.with_structured_output(BusinessCard)
            result = llm_structured.invoke({"b64":img_b64, "type" : mime_type})
            # 6. 결과 출력
            print("상호 :", result.company)
            print("이름 :", result.name)
            print("전화 :", result.phone)
            print("이메일 :", result.email)
            print("주소 :", result.address)
        else:
            print("이미지 확장자 jpg, jpeg, png만 가능합니다")
    else:
        print("찾는 명함이 없습니다!!!")
