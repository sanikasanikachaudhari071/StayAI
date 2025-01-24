from pydantic import BaseModel
from typing import List, Optional


class Conversation(BaseModel):
    role: Optional[str]
    content: Optional[str]

class ChatRequest(BaseModel):
    user_id: str
    user_query: str
    messages: List[Conversation]

class ChatResponse(BaseModel):
    response: str