import requests
import os
from dotenv import load_dotenv
from typing import List
from backend.embeddings.base_embedding import BaseEmbedding, EmbeddingInput

load_dotenv()


class JinaEmbeddingInput(EmbeddingInput):
    task: str = "text-matching"
    late_chunking: bool = False
    URL: str = "https://api.jina.ai/v1/embeddings"
    headers: dict[str, str] = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.getenv("JINA_API_KEY")}',
    }


class JinaEmbedding(BaseEmbedding):
    def __init__(self, embedding_input: JinaEmbeddingInput) -> None:
        super().__init__(embedding_input)

    def _call_embedding_model(self, texts: List[str]) -> List[List[float]]:
        data = {
            "model": self._input.model_name,
            "task": self._input.task,
            "late_chunking": self._input.late_chunking,
            "dimensions": self._input.dimensions,
            "embedding_type": self._input.embedding_type,
            "input": texts,
        }
        response = requests.post(
            self._input.URL, headers=self._input.headers, json=data
        )
        return self._parse_jina_response(response.json())

    def _parse_jina_response(self, response: dict) -> List[List[float]]:
        result = []
        for embedding in response["data"]:
            result.append(embedding["embedding"])
        return result


if __name__ == "__main__":
    input = JinaEmbeddingInput(
        model_name="jina-embeddings-v3",
        task="text-matching",
        late_chunking=False,
        dimensions=1024,
        embedding_type="float",
    )
    embedding = JinaEmbedding(input)
    embedding_outputs: List[List[float]] = embedding.generate_batch_embeddings(
        ["Hello, how are you?", "I am arkajit datta"]
    )

    # Calculate cosine similarity between the two embeddings
    similarity: float = embedding.calculate_cosine_similarity(
        embedding_outputs[0], embedding_outputs[1]
    )
    print(f"Cosine similarity: {similarity}")
