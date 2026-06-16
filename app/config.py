"""集中读取环境变量。所有配置从这里取，别在业务代码里散落 os.getenv。"""
import os

from dotenv import load_dotenv

# 启动时把 .env 加载进环境变量
load_dotenv()


class Settings:
    api_key: str = os.getenv("LLM_API_KEY", "")
    base_url: str = os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
    model: str = os.getenv("LLM_MODEL", "deepseek-chat")


settings = Settings()
