from fastapi import FastAPI
from backend.routes import generate_image

app = FastAPI()

app.include_router(generate_image.router)