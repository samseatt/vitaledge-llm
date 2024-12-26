# app/services/service_factory.py

from app.core.config import Config, config
from app.services.llama_service import LlamaService
from app.services.openai_service import OpenAIService
from app.services.mock_service import MockService
import logging

logger = logging.getLogger(__name__)

# Global variable to hold the current LLM service
_llm_service = None

def get_llm_service():
    """
    Get the current LLM service instance. Initialize if not already set.
    """
    global _llm_service
    if _llm_service is None:
        _llm_service = _initialize_llm_service()
    return _llm_service

def _initialize_llm_service():
    """
    Initialize the LLM service based on the configured backend.
    """
    logger.info(f"Initializing LLM backend: {Config.LLM_BACKEND}")
    if Config.LLM_BACKEND == "llama":
        return LlamaService()
    elif Config.LLM_BACKEND == "openai":
        return OpenAIService(api_key=config.OPENAI_API_KEY)
    elif Config.LLM_BACKEND == "mock":
        return MockService()
    else:
        raise ValueError(f"Unsupported LLM backend: {Config.LLM_BACKEND}")

def reset_llm_service():
    """
    Reset the LLM service instance. Use this to reload the service dynamically.
    """
    global _llm_service
    _llm_service = _initialize_llm_service()
