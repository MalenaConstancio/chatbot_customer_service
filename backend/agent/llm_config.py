from langchain_openai import ChatOpenAI
from backend.config.settings import Settings

settings = Settings()

def get_llm():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        api_key=settings.OPENAI_API_KEY
    )
