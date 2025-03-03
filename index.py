from fast_alpr import ALPR
import os, shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Annotated

# You can also initialize the ALPR with custom plate detection and OCR models.
alpr = ALPR(
    detector_model="yolo-v9-t-384-license-plate-end2end",
    ocr_model="global-plates-mobile-vit-v2-model",
)
app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    file_path = os.path.join("images/", file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")
    finally:
        file.file.close()

    alpr_results = alpr.predict("images/"+file.filename)
    return {"message": alpr_results}
