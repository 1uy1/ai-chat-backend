"""AI Chat Backend —— 第一条链路：接收提问 → 调大模型 → 返回回复。"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
from pydantic import BaseModel

from app.config import settings

app = FastAPI(title="AI Chat Backend", version="0.1.0")

# OpenAI 兼容客户端，base_url 指向 DeepSeek（或任意兼容服务）
client = AsyncOpenAI(api_key=settings.api_key, base_url=settings.base_url)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def health():
    """健康检查，确认服务活着。"""
    return {"status": "ok", "model": settings.model}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """多轮对话：接收历史消息列表，整个发给大模型。"""
    try:
        resp = await client.chat.completions.create(
            model=settings.model,
            messages=[m.model_dump() for m in req.messages],
        )
    except Exception as e:
        # Key 失效、超时、网络问题等都在这里兜住，返回友好报错
        raise HTTPException(status_code=502, detail=f"调用大模型失败: {e}")

    return ChatResponse(reply=resp.choices[0].message.content)

@app.post("/chat/stream")
async def chat_stream(req:ChatRequest):
    """流式对话：模型边生成边推送，打字机效果。"""
    async def event_generator():
        try:
            stream = await client.chat.completions.create(
                model = settings.model,
                messages = [m.model_dump() for m in req.messages],
                stream = True,
            )
            async for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield f"data:{delta}\n\n"
        except Exception as e:
            yield f"data:[ERROR {e}\n\n]"
    return StreamingResponse(event_generator(),media_type="text/event-stream")