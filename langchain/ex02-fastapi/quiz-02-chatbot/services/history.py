from langchain_core.messages import HumanMessage, AIMessage

history : list = []
_store : dict[ str, list ] = {}
"""
_store = {
    "aaa":[human(내이름 홍길동), ai( 반가원 길동아)],
    "bbb":[]
    "ccc":[]
}
_store.get( user_id ) => []
"""

def get_history( username : str ) -> list:
    if username not in _store:
        _store[username] = []
    return _store[username]


def add_turn(username:str, user_msg: str, ai_msg: str ) -> None:
    """사용자 입력과 AI 응답을 이력에 추가한다."""
    history = get_history(username)
    history.append(HumanMessage(content=user_msg))
    history.append(AIMessage(content=ai_msg))
