from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.rag import rag_answer

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = rag_answer(q)
    # 确保返回 UTF-8 编码的 JSON 响应
    return JSONResponse(
        content={"answer": answer},
        media_type="application/json; charset=utf-8"
    )
