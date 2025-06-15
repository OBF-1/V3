from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
import piexif

router = APIRouter()

@router.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are supported.")

    content = await file.read()
    file_size = len(content)

    try:
        image = Image.open(io.BytesIO(content))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    metadata = {
        "filename": file.filename,
        "content_type": file.content_type,
        "format": image.format,
        "mode": image.mode,
        "size": image.size,
        "width": image.width,
        "height": image.height,
        "file_size_bytes": file_size
    }

    try:
        exif_data = piexif.load(image.info.get("exif", b""))
        readable_exif = {}
        for ifd in exif_data:
            for tag in exif_data[ifd]:
                key = piexif.TAGS[ifd][tag]["name"]
                value = exif_data[ifd][tag]
                readable_exif[key] = value
        metadata["exif"] = readable_exif
    except Exception:
        metadata["exif"] = "No EXIF metadata found."

    return metadata
