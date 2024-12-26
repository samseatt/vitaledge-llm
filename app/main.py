# app/main.py

from fastapi import FastAPI
from app.api.routes.generation import router as generation_router
from app.api.routes.embeddings import router as embeddings_router
from app.api.routes.admin import router as admin_router

app = FastAPI(title="VitalEdge LLaMA Service")

# Include routes
app.include_router(generation_router, prefix="/llm", tags=["generation"])
app.include_router(embeddings_router, prefix="/llm", tags=["embeddings"])
app.include_router(admin_router, prefix="/admin", tags=["get_model"])
app.include_router(admin_router, prefix="/admin", tags=["set_model"])

@app.get("/health")
def health():
    return {"status": "healthy"}
