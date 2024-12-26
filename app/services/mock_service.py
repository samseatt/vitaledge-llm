# app/services/mock_service.py

from typing import List
from app.utils.logger import logger
from app.services.base_llm import BaseLLM

class MockService(BaseLLM):
    def generate_text(self, input_text: str, max_length: int = 50) -> str:
        logger.info(f"Returning mock response for input: {input_text}")
        return f"Mock response for: {input_text}"

    def generate_embeddings(self, input_texts: List[str]) -> List[List[float]]:
        logger.info(f"Returning mock embedding for input: {input_texts[0]}")
        return f"Mock embeddings for: {input_texts}"

# mock_service = MockService()
