# PROGRESS

校招求职主线项目进度清单。每完成一项打勾并 commit。

## 阶段 0：开工准备
- [x] 新建独立项目目录 `ai-chat-backend`
- [x] 写最简 README（项目名 + 一句话目标）
- [x] `.env` + `.gitignore`（密钥不入库）
- [ ] git init + 关联 GitHub 远程（public）
- [ ] 第一个 commit：`init project`
- [ ] 准备好大模型 API Key，填进 `.env`

## 阶段 1：最小链路（第 1 周）
- [x] 装好 fastapi / uvicorn / openai
- [x] `/chat` POST 接口：接收 message → 调大模型 → 返回回复
- [ ] 在 `/docs` 里调通 `/chat`
- [ ] commit: `feat: basic /chat endpoint`
- [ ] 搞懂 async/await，把 `/chat` 改成异步
- [ ] commit: `refactor: async LLM call`
- [ ] 多轮对话（接收历史消息列表）
- [ ] 流式输出 SSE（打字机效果）
- [ ] commit: `feat: multi-turn chat + streaming`

**第 1 周验收**：从零启动服务，完整演示一次多轮 + 流式对话。

## 阶段 2：RAG + 持久化（第 2–3 周）
- [ ] SQLAlchemy + SQLite，conversations / messages 两张表
- [ ] 对话历史入库，按会话 ID 读历史
- [ ] commit: `feat: persist chat history with SQLAlchemy`
- [ ] `/upload` 接口 + 文档切分 + 向量化 + 存向量库
- [ ] 检索相关片段 → 拼 prompt → 带依据答案
- [ ] commit: `feat: RAG - upload, embed, retrieve, answer`
- [ ] function calling / 工具调用
- [ ] commit: `feat: agent tool calling`

## 阶段 3：工程化 + 包装（第 4 周）
- [ ] 项目分层（路由 / 业务 / 数据库 / 配置）
- [ ] Dockerfile + docker-compose.yml 一键启动
- [ ] 加分项：Redis 缓存/限流 或 JWT 鉴权（任选）
- [ ] 完善 README（架构图、截图、API 说明）
- [ ] commit: `chore: dockerize + docs`

**第 1 月验收**：别人 clone 仓库，照 README 能一键跑起来。

## 常驻任务
- [ ] 每天 1–2 题 LeetCode
- [ ] 每天 30 分钟八股（只补当周项目相关）
- [ ] 每周至少 push 一次，commit 用 feat/fix/docs/refactor 前缀
