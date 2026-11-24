from fastapi import FastAPI
from routes import chat_router
import uvicorn
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="스트리밍 챗봇")
# 라우터 등록
app.include_router(chat_router.router)

# static/index.html 경로
_INDEX = Path(__file__).parent / "static" / "index.html"

@app.get("/")
async def index():
    return FileResponse(_INDEX)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
