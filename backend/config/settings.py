from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERPAPI_API_KEY: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
