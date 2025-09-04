import os
import sys
import fitz  # PyMuPDF 라이브러리


def convert_pdf_to_images(pdf_path, output_dir, image_format="jpg"):
    """
    PDF 파일의 각 페이지를 이미지로 변환합니다.

    :param pdf_path: 입력 PDF 파일의 경로입니다.
    :param output_dir: 출력 이미지를 저장할 디렉터리입니다.
    :param image_format: 출력 이미지의 형식입니다 (예: 'jpg', 'png').
    """
    # PDF 파일이 존재하는지 확인합니다.
    if not os.path.isfile(pdf_path):
        print(f"오류: '{pdf_path}'에서 PDF 파일을 찾을 수 없습니다.")
        sys.exit(1)

    # 출력 디렉터리가 존재하지 않으면 생성합니다.
    os.makedirs(output_dir, exist_ok=True)

    # 출력 이미지의 파일명을 만들기 위해 PDF 파일의 기본 이름을 가져옵니다.
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    doc = None  # doc 변수를 None으로 초기화합니다.
    try:
        # PDF 파일을 엽니다.
        doc = fitz.open(pdf_path)
        print(f"'{pdf_path}' 파일을 {image_format} 형식으로 변환 중입니다...")

        # 각 페이지를 반복하며 이미지로 저장합니다.
        for page_num, page in enumerate(doc):
            pix = page.get_pixmap()
            output_image_path = os.path.join(
                output_dir,
                f"{pdf_filename}_page_{page_num + 1}.{image_format}"
            )
            pix.save(output_image_path)

        print(f"성공적으로 {len(doc)} 페이지를 변환했습니다.")
        print(f"이미지가 '{os.path.abspath(output_dir)}'에 저장되었습니다.")

    except Exception as e:
        print(f"PDF 처리 중 오류가 발생했습니다: {e}")
        sys.exit(1)
    finally:
        if doc:
            doc.close()

def main():
    """PDF 변환을 직접 실행하는 메인 함수입니다."""
    # 스크립트가 있는 디렉터리를 기준으로 경로를 설정합니다.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_source_dir = os.path.join(script_dir, "pdf") # PDF 파일이 있는 폴더
    # 이미지를 저장할 폴더 (스크립트 위치 아래에 'image' 폴더)
    output_directory = os.path.join(script_dir, "image")
    # 변환할 이미지 포맷
    image_format_to_use = "jpg"

    # PDF 소스 디렉터리가 존재하는지 확인합니다.
    if not os.path.isdir(pdf_source_dir):
        print(f"오류: PDF 소스 폴더 '{pdf_source_dir}'를 찾을 수 없습니다.")
        print("스크립트와 동일한 위치에 'pdf' 폴더를 만들고 그 안에 PDF 파일들을 넣어주세요.")
        return

    # pdf 폴더에서 .pdf 파일을 모두 찾습니다.
    pdf_files = [f for f in os.listdir(pdf_source_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"'{pdf_source_dir}' 폴더에서 변환할 PDF 파일을 찾을 수 없습니다.")
        return

    print(f"총 {len(pdf_files)}개의 PDF 파일을 변환합니다.")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_source_dir, pdf_file)
        print(f"\nStarting conversion for: {pdf_path}")
        convert_pdf_to_images(pdf_path, output_directory, image_format_to_use)

if __name__ == "__main__":
    main()
