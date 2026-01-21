from langchain_openai import ChatOpenAI
from app.config.settings import settings

def get_llm():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY,
        request_timeout=30,
        max_retries=2,
        streaming=False
    )
