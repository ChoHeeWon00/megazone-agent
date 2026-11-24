from langchain_core.messages import HumanMessage, AIMessage

history : list = []

def add_turn( user_msg: str, ai_msg: str ) -> None:
    """사용자 입력과 AI 응답을 이력에 추가한다."""
    history.append(HumanMessage(content=user_msg))
    history.append(AIMessage(content=ai_msg))
