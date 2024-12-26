# app/api/routes/__init__.py

from fastapi import APIRouter
from app.api.routes import generation, embeddings, admin

router = APIRouter()
router.include_router(generation.router, prefix="/llm", tags=["Generation"])
router.include_router(embeddings.router, prefix="/llm", tags=["Embeddings"])
router.include_router(admin.router, prefix="/set_model", tags=["Admin"])
router.include_router(admin.router, prefix="/get_model", tags=["Admin"])
