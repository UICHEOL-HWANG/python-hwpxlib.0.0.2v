from dto.schemas import ExtractTextResponse
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from utils.extract import process_hwp
import os
import uuid
import shutil

router = APIRouter(
    prefix="/v1",
    tags=["extract-text"]
)

UPLOAD_DIR = "/app/uploads"
HWPX_JAR_PATH = "/app/hwpxlib-1.0.5.jar"
WORK_DIR = "/app"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/extract", summary="HWPX 텍스트 추출", description="업로드된 HWPX 파일에서 텍스트를 추출합니다.")
async def extract_text(file: UploadFile = File(...)):
    if not file.filename.endswith(".hwpx"):
        raise HTTPException(status_code=400, detail="HWPX 파일만 지원합니다.")

    # 임시 저장
    unique_filename = f"{uuid.uuid4().hex}.hwpx"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 추출 실행
    result = process_hwp(file_path, HWPX_JAR_PATH, WORK_DIR)

    # 파일 삭제
    os.remove(file_path)

    # 오류 처리
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return JSONResponse(content=result)