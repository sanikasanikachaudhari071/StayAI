import os
from typing import List, Dict
from groq import Groq
from groq.types.chat.chat_completion import ChatCompletion


class GroqInference:
    def __init__(self, model: str = "llama-3.3-70b-versatile") -> None:
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
        self.groq_client = Groq()
        self.model = model

    def generate_response(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.1,
        max_tokens: int = 512,
        top_p: float = 1.0,
        stream: bool = False,
        stop: List[str] = None,
    ) -> str:
        """
        Generate a response using Groq's LLM.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys

        Returns:
            str: The generated response from the model
        """
        completion: ChatCompletion = self.groq_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=stream,
            stop=stop,
        )
        return completion.choices[0].message.content