# python-hwpxlib.0.0.2v

# HWPX 파서 API

[한국어](./README_ko.md) | [English](./README.md)

> 이 프로젝트는 [python-hwpxlib](https://github.com/choijhyeok/python-hwpxlib)의 구조를 개선하여 FastAPI 기반으로 리팩토링한 HWPX 파서입니다. 더 편리하게 `.hwpx` 파일을 처리하고 연동할 수 있도록 설계되었습니다.

이 프로젝트는 `.hwpx` 문서에서 텍스트를 추출하는 FastAPI 기반의 API 서비스를 제공합니다. 내부적으로는 Java 기반의 `hwpxlib`를 `jpype`를 통해 호출하여 텍스트를 추출합니다.

---

## 📦 주요 기능

- `.hwpx` 파일의 본문 텍스트 추출
- Java `hwpxlib` 연동 (`jpype` 사용)
- FastAPI로 RESTful API 제공
- Docker를 통한 간편한 배포
- 컨테이너 내 UTF-8 및 한글 인코딩 완벽 지원

---

## 🚀 사용 방법

### 1. 레포지토리 클론

```bash
git clone https://github.com/UICHEOL-HWANG/python-hwpxlib.0.0.2v.git

cd python-hwpxlib.0.0.2v
```

### 2. 컨테이너 빌드 
```bash
docker compose up --build -d
```

### API에 파일 전송 
```python
import requests

url = "http://localhost:7860/v1/extract"
file_path = "your_file.hwpx"

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

print(response.json())
```

### 최종 응답 

```json
{
    "filename": "document.hwpx",
    "text": "이것은 추출된 HWPX 문서의 본문 텍스트입니다.\n여러 문단이 포함될 수 있습니다.\n표, 리스트, 각주 등도 함께 처리됩니다."
}
```

