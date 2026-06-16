"""AI Chat Backend —— 第一条链路：接收提问 → 调大模型 → 返回回复。"""
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

from app.config import settings

app = FastAPI(title="AI Chat Backend", version="0.1.0")

# OpenAI 兼容客户端，base_url 指向 DeepSeek（或任意兼容服务）
client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def health():
    """健康检查，确认服务活着。"""
    return {"status": "ok", "model": settings.model}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """最简单的单轮对话：一句话进，一句话出。"""
    try:
        resp = client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "user", "content": req.message}],
        )
    except Exception as e:
        # Key 失效、超时、网络问题等都在这里兜住，返回友好报错
        raise HTTPException(status_code=502, detail=f"调用大模型失败: {e}")

    return ChatResponse(reply=resp.choices[0].message.content)
