# AI Chat Backend

一个基于 FastAPI 的大模型应用后端，支持多轮对话和 RAG。

## 技术栈

FastAPI · async · SQLAlchemy/SQLite · 向量库(Chroma/FAISS) · 大模型 API(OpenAI 兼容) · Docker

## 快速开始

```bash
# 1. 创建并激活虚拟环境
py -m venv .venv
source .venv/Scripts/activate    # Windows Git Bash
# .venv\Scripts\activate         # Windows PowerShell/CMD

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置密钥：复制 .env.example 为 .env，填入你的 API Key
cp .env.example .env

# 4. 启动服务
uvicorn app.main:app --reload

# 5. 打开交互文档调试
# http://127.0.0.1:8000/docs
```

## API

| 方法 | 路径    | 说明           |
|------|---------|----------------|
| GET  | `/`     | 健康检查       |
| POST | `/chat` | 单轮对话       |

请求示例：

```json
POST /chat
{ "message": "你好，介绍一下你自己" }
```

## 进度

见 [PROGRESS.md](PROGRESS.md)。
