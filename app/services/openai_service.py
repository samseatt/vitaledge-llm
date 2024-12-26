# app/services/openai_service.py

from openai import OpenAI
from typing import List
from app.utils.logger import logger
from app.services.base_llm import BaseLLM

class OpenAIService(BaseLLM):
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        logger.info("Initializing OpenAI GPT-4o client...")
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_text(self, input_text: str, max_length: int = 400) -> str:
        logger.info(f"Generating text with OpenAI GPT-4o for: {input_text}")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text},
            ],
            max_tokens=max_length,
        )
        return response.choices[0].message.content

    def generate_embeddings(self, input_texts: List[str]) -> List[List[float]]:
        response = self.client.embeddings.create(
            model=self.model,
            input=input_texts
        )
        return [embedding.embedding for embedding in response.data]

# openai_service = OpenAIService(api_key=config.OPENAI_API_KEY)
