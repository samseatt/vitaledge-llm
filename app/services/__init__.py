# app/services/__init__.py

from .service_factory import get_llm_service, reset_llm_service

# llm_service = get_llm_service()


# from app.core.config import config
# from app.services.llama_service import LlamaService
# from app.services.openai_service import OpenAIService
# from app.services.mock_service import MockService

# def get_llm_service():
#     if config.LLM_BACKEND == "llama":
#         return LlamaService()
#     elif config.LLM_BACKEND == "openai":
#         return OpenAIService(api_key=config.OPENAI_API_KEY)
#     elif config.LLM_BACKEND == "mock":
#         return MockService()
#     else:
#         raise ValueError("Invalid LLM backend specified in config")

# llm_service = get_llm_service()

