# app/core/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3.2-1B-Instruct")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "no-key-supplied")
    LLM_BACKEND = os.getenv("LLM_BACKEND", "llama")  # 'llama', 'openai', 'mock'

config = Config()
