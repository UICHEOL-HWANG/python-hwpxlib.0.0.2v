import uvicorn
from router.api import router
from fastapi import FastAPI

app = FastAPI(
    title = "HWPX 추출기",
    version = "1.0",
    description="한글 HWPX 문서를 단순 텍스트로 몽땅 뽑아내는 API 입니다."
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)