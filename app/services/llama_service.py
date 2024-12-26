# app/services/llama_service.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from app.utils.logger import logger
from typing import List
from app.core.config import config
from app.services.base_llm import BaseLLM

class LlamaService(BaseLLM):
    def __init__(self):
        logger.info("Loading LLaMA model...")
        self.tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(
            config.MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="cpu"  # Adjust for GPU if available
        )
        # self.model.eval()
        logger.info("LLaMA model loaded successfully.")

    def generate_text(self, input_text: str, max_length: int = 200) -> str:
        logger.info(f"Generating text for input: {input_text}")
        inputs = self.tokenizer(input_text, return_tensors="pt").to("cpu")
        outputs = self.model.generate(**inputs, max_length=max_length)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        logger.info(f"Generated text: {result}")
        return result

    def generate_embeddings(self, input_texts: List[str]) -> List[List[float]]:
        logger.info(f"Generating embeddings for input: {input_texts[0]} ...")
        embeddings = []
        with torch.no_grad():
            for text in input_texts:
                inputs = self.tokenizer(text, return_tensors="pt").to("cpu")
                outputs = self.model(**inputs)
                embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().tolist())
        return embeddings
        
# llama_service = LlamaService()
