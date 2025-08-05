# python-hwpxlib.0.0.2v

# HWPX Parser API

[한국어](./README_ko.md) | [English](./README.md)



This project provides an API service built with FastAPI that extracts text from `.hwpx` documents using [python-hwpxlib](https://github.com/choijhyeok/python-hwpxlib) and Java `hwpxlib`.

---

## 📦 Features

- Extracts plain text from `.hwpx` files
- Uses Java-based `hwpxlib` via `jpype`
- Provides RESTful API with FastAPI
- Docker-based deployment
- Supports UTF-8 / Korean encoding in container

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/UICHEOL-HWANG/python-hwpxlib.0.0.2v.git

cd python-hwpxlib.0.0.2
```

### 2. build a container 
```bash 
docker compose up --build -d 
```

### 3. Send File to API

```python 
import requests

url = "http://localhost:7860/v1/extract"
file_path = "your_file.hwpx"

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

print(response.json())

```

### Response 

```json
{
    "filename": "document.hwpx",
    "text": "this is document extract"
}
```