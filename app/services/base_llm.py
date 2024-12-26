# app/services/base_llm.py

from abc import ABC, abstractmethod
from typing import List

class BaseLLM(ABC):
    @abstractmethod
    def generate_text(self, input_text: str, max_length: int = 200) -> str:
        """Generate text based on input."""
        pass

    @abstractmethod
    def generate_embeddings(self, input_texts: List[str]) -> List[List[float]]:
        """Generate embeddings for input texts."""
        pass
