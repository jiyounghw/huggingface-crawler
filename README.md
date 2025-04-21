# 🤗 Hugging Face Model Crawler

Hugging Face에 공개된 AI/ML 모델의 메타 정보를 수집하는 Python 기반 웹 크롤러

---

## Introduction

- Hugging Face 플랫폼 기반의 모델 메타데이터 수집
- URL 기반 모델 정보 수집 및 CSV 저장
- 모델의 태그, model card, 연동된 Space 정보 수집

---

## Data

- 사전 수집된 모델 URL 리스트 파일: `data/urls_3000_common_250201.csv`

---
## 사용 라이브러리

- `requests`  
- `beautifulsoup4`  
- `tqdm`  
- `pandas`  
- `re`

설치 명령어:

```bash
pip install requests beautifulsoup4 tqdm pandas
```

---

## 실행방법
```bash
python huggingface_crawler.py
```
