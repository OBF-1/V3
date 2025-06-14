from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.image_service import generate_image

router = APIRouter()

class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    width: int = 1024
    height: int = 1024
    steps: int = 30
    guidance: float = 7.5
    seed: int = -1
    model: str = "sdxl"
    use_lora: bool = False
    preview: bool = False

@router.post("/generate-image")
def image_generation_endpoint(req: ImageRequest):
    try:
        result = generate_image(req)
        return {"status": "success", "path": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))