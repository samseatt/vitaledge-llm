# app/api/routes/embeddings.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.service_factory import get_llm_service

router = APIRouter()

class EmbeddingsRequest(BaseModel):
    texts: List[str]

@router.post("/embeddings", tags=["Embeddings"])
def generate_embeddings(request: EmbeddingsRequest):
    """
    Generate embeddings for input texts.
    """
    try:
        llm_service = get_llm_service()
        embeddings = llm_service.generate_embeddings(request.texts)
        return {"embeddings": embeddings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# from fastapi import APIRouter
# from pydantic import BaseModel
# from typing import List

# router = APIRouter()

# class EmbeddingsRequest(BaseModel):
#     texts: List[str]

# class EmbeddingsResponse(BaseModel):
#     embeddings: List[List[float]]

# @router.post("/embeddings", response_model=EmbeddingsResponse)
# async def generate_embeddings(request: EmbeddingsRequest):
#     """
#     Mock endpoint for generating embeddings using Llama.
#     """
#     mock_embedding = [0.1, 0.2, 0.3]  # Replace with actual dimensions later
#     return {"embeddings": [mock_embedding for _ in request.texts]}
