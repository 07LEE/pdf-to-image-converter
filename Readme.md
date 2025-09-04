# PDF를 이미지로 변환하는 스크립트

## 설명

이 스크립트는 지정된 폴더에 있는 모든 PDF 파일을 이미지 파일(JPG 형식)으로 변환합니다.

## 폴더 구조

스크립트가 올바르게 작동하려면 다음 폴더 구조를 따라야 합니다:

```
pdf_to_image/
├── pdf/
│   ├── example1.pdf
│   └── example2.pdf
├── image/
│   └── (출력 이미지를 저장하기 위해 자동으로 생성되는 폴더)
├── pdf_to_jpg.py
└── requirements.txt
```

-   **`pdf/`**: 변환하려는 모든 PDF 파일을 이 폴더에 넣으세요.
-   **`image/`**: 변환된 JPG 이미지 파일이 여기에 저장됩니다.

## 설치 방법

1.  Python이 설치되어 있는지 확인하세요.
2.  pip를 사용하여 필요한 라이브러리를 설치하세요:

    ```bash
    pip install -r requirements.txt
    ```
    `requirements.txt` 파일에는 다음 라이브러리가 포함되어 있습니다:
    - `PyMuPDF`

## 사용 방법

1.  `pdf` 폴더에 PDF 파일들을 넣으세요.
2.  터미널에서 스크립트를 실행하세요:

    ```bash
    python pdf_to_jpg.py
    ```

3.  스크립트는 `pdf` 폴더의 모든 PDF 파일을 찾아 JPG 이미지로 변환한 다음 `image` 폴더에 저장합니다.