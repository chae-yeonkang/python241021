import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 각 파일 유형에 맞는 폴더 경로
image_folder = r'C:\Users\student\Downloads\images'
data_folder = r'C:\Users\student\Downloads\data'
docs_folder = r'C:\Users\student\Downloads\docs'
archive_folder = r'C:\Users\student\Downloads\archive'

# 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)   # 이미지 파일 폴더
os.makedirs(data_folder, exist_ok=True)    # 데이터 파일 폴더
os.makedirs(docs_folder, exist_ok=True)    # 문서 파일 폴더
os.makedirs(archive_folder, exist_ok=True) # 압축 파일 폴더

# 파일 이동 함수
def move_file(file_name, src_folder, dest_folder):
    """
    파일을 지정된 폴더로 이동하는 함수
    :param file_name: 이동할 파일 이름
    :param src_folder: 원본 파일 폴더
    :param dest_folder: 파일을 이동할 대상 폴더
    """
    src_path = os.path.join(src_folder, file_name)
    dest_path = os.path.join(dest_folder, file_name)

    # 파일을 대상 폴더로 이동
    shutil.move(src_path, dest_path)
    print(f"{file_name} 파일이 {dest_folder}로 이동되었습니다.")

# 다운로드 폴더에서 파일 검사 및 이동
for file_name in os.listdir(download_folder):
    # 각 파일의 절대 경로 생성
    file_path = os.path.join(download_folder, file_name)

    # 파일인 경우에만 처리
    if os.path.isfile(file_path):
        # 확장자별로 해당 폴더로 이동
        if file_name.lower().endswith(('.jpg', '.jpeg')):
            move_file(file_name, download_folder, image_folder)
        elif file_name.lower().endswith(('.csv', '.xlsx')):
            move_file(file_name, download_folder, data_folder)
        elif file_name.lower().endswith(('.txt', '.doc', '.pdf')):
            move_file(file_name, download_folder, docs_folder)
        elif file_name.lower().endswith('.zip'):
            move_file(file_name, download_folder, archive_folder)
