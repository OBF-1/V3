from fastapi import FastAPI
from backend.routes import analyze_image

app = FastAPI(title="V3 Backend", version="3.1")

@app.get("/")
def root():
    return {"message": "V3 backend running"}

app.include_router(analyze_image.router)
