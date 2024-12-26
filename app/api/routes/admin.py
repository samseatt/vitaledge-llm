# app/api/routes/admin.py

from fastapi import APIRouter, HTTPException
from app.core.config import Config
from app.services.service_factory import reset_llm_service
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/set_model", tags=["Admin"])
def set_model(backend: str):
    """
    Dynamically update the LLM backend.
    """
    try:
        logger.info(f"Switching model from {Config.LLM_BACKEND} to {backend}")
        # Validate the backend
        if backend not in ["llama", "openai", "mock"]:
            raise ValueError(f"Unsupported backend: {backend}")

        # Update the backend configuration
        Config.LLM_BACKEND = backend

        # Reset the LLM service to reflect the change
        reset_llm_service()

        return {"message": f"Backend successfully updated to: {backend}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_model", tags=["Admin"])
def get_current_model():
    """
    Endpoint to return the currently active LLM backend.
    """
    logger.info(f"Getting model for {Config.LLM_BACKEND}")
    return {"current_model": Config.LLM_BACKEND}