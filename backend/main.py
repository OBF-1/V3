
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="V3 Upload Test", version="0.1.0")

@app.get("/")
def root():
    return {"message": "V3 backend running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content)
    })
