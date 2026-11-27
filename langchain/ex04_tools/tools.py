from langchain_core.tools import tool

@tool
def get_weather(city:str) -> str:
    """도시의 현재 날씨를 반환한다"""
    print("--- get_weather 호출 ---")
    return {"서울":"맑음 12도","부산":"흐림 5도"}.get(city,"정보 없음")

@tool
def multiply(a: int, b: int) -> int:
    """두 정수 a와 b를 곱한(곱하기) 값을 반환한다. 곱셈 계산이 필요할 때 사용한다."""
    return a * b

