from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm_config import get_llm

# 할 일 하나 (중첩 모델)
class Task(BaseModel):
    title: str = Field(description="할 일 내용 (예: 디자인, 개발)")
    owner: str = Field(description="담당자 이름")
    due: str = Field(description="기한 (예: 수요일, 금요일)")

# 전체 계획 (Task 리스트를 가짐)
class Plan(BaseModel):
    project: str = Field(description="프로젝트 이름")
    tasks: list[Task] = Field(description="할 일 목록")

parser = PydanticOutputParser(pydantic_object=Plan)

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
        너는 회의 메모에서 할 일을 추출하는 도우미야.
        반드시 아래 형식의 JSON으로만 답해.
        최상위에 'project'와 'tasks'를 반드시 포함해.
        project는 메모의 프로젝트 이름으로 채우고,
        tasks는 title, owner, due를 가진 객체 배열이야.
        {format}
     """),
    ("human", "{memo}"),
]).partial(format=parser.get_format_instructions())

chain = prompt | llm | parser

memo = "신제품 출시 프로젝트. 디자인은 길동이가 수요일까지, 개발은 지은이가 금요일까지."
r = chain.invoke({"memo": memo})


line = f"\n프로젝트 : {r.project}\n"
line += "=="*20+"\n"
for task in r.tasks:
    line += f"owner : {task.owner}\n"
    line += f"title : {task.title}\n"
    line += f"due : {task.due}\n"
    line += "--"*20+"\n"
print(line)
