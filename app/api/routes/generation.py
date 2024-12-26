# app/api/routes/generation.py

from fastapi import APIRouter, HTTPException
from app.services import get_llm_service

router = APIRouter()

@router.post("/generate", tags=["Generation"])
def generate_text(payload: dict):
    print(f"generate_text route called with payload dict: {payload}")
    input_text = payload.get("prompt", "")
    if not input_text:
        raise HTTPException(status_code=400, detail="Missing 'prompt' in payload.")
    
    llm_service = get_llm_service()
    return {"response": llm_service.generate_text(input_text)}
