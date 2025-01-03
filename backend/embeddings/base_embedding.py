from typing import List, Type
from pydantic import BaseModel
from abc import ABC, abstractmethod
import numpy as np


class EmbeddingInput(BaseModel):
    model_name: str
    dimensions: int
    embedding_type: str


class BaseEmbedding(ABC):
    def __init__(self, embedding_input: Type[EmbeddingInput]) -> None:
        self._input: EmbeddingInput = embedding_input

    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text (str): The text to generate embedding for.

        Returns:
            List[float]: The embedding for the text.
        """
        embeddings: List[List[float]] = self._call_embedding_model([text])
        return embeddings[0]

    def generate_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.

        Args:
            texts (List[str]): The list of texts to generate embeddings for.

        Returns:
            List[List[float]]: The embeddings for the list of texts.
        """
        embeddings: List[List[float]] = self._call_embedding_model(texts)
        return embeddings

    @abstractmethod
    def _call_embedding_model(self, texts: List[str]) -> List[List[float]]:
        pass

    def calculate_cosine_similarity(
        self, embedding1: List[float], embedding2: List[float]
    ) -> float:
        """
        Calculate cosine similarity between two embeddings.

        Args:
            embedding1 (List[float]): First embedding vector
            embedding2 (List[float]): Second embedding vector

        Returns:
            float: Cosine similarity score between -1 and 1, where 1 means most similar
        """
        # Convert lists to numpy arrays for efficient computation
        vec1 = np.array(embedding1)
        vec2 = np.array(embedding2)

        # Calculate cosine similarity: dot product divided by the product of norms
        similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

        return float(similarity)
