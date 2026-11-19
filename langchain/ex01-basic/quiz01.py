import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage

TONS = {
    "1":"강아지 말두로 답변한다. 마지막에 멍멍을 넣는다",
    "2":"고양이 말투로 답변한다. 마지막에 야옹을 넣는다",
    "3":"정중하고 친절한 존댓말로 답변한다",
}

llm = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

print("=== exit 종료 ===")

while True:
    print() #단순 엔터 적용
    #dict = { "name" : "홍길동"} => dict.get("name")
    tone = TONS.get( input("말투 선택(1.강아지, 2.고양이, 3.정중한 : )"))
    #print( tone )
    q = input("나 입력(exit) : ")
    #print( q )
    #print( q.lower() == "exit" )
    if q.lower() == "exit":
        print("종료")
        break

    messages = [
        SystemMessage(content=f"""
            너는 친절한 AI 비서다
            {tone}
            반드시 tone에 작성된 내용으로 답변한다
            사용자의 질문에 정확하게 답변한다.
            한문장으로 답변한다
        """),
        HumanMessage(content=q)
    ]
    result = llm.stream( messages )
    for chunk in result:
        print( chunk.text , end="" )










