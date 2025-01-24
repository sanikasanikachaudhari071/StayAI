import uvicorn
from typing import List, Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.models import ChatRequest, ChatResponse, Conversation
from backend.conversation.chat import chat_with_travel_assistant

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"message": "Hello World"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    user_id = request.user_id
    user_query = request.user_query
    messages = request.messages
    processed_messages = process_messages(messages)
    assistant_answer, messages = chat_with_travel_assistant(
        user_id, user_query,   processed_messages
    )
    return ChatResponse(response=assistant_answer)


def process_messages(messages: List[Conversation]) -> List[Dict[str, str]]:
    return [{"role": message.role, "content": message.content} for message in messages]

