from pydantic import BaseModel

class UserQuery(BaseModel):
    query: str
    chat_history: list = []