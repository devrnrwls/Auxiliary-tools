import os

from PIL import Image
import os

def convert_jpg_to_png(input_path, output_path):
    # 이미지 로드
    image = Image.open(input_path)

    # 저장할 경로와 파일 이름 설정
    output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".png"
    output_file_path = os.path.join(output_path, output_filename)

    # 이미지를 png로 변환하여 저장
    image.save(output_file_path, format="PNG")

    return output_file_path

def convert_all_jpg_to_png(input_folder, output_folder):
    # 출력 폴더가 없으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 입력 폴더 내의 모든 파일 순회
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)

        # jpg 파일이면 png로 변환하고 원래 파일 삭제
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            output_file_path = convert_jpg_to_png(input_file_path, output_folder)
            print(f"{filename} 변환 완료: {output_file_path}")

# 테스트를 위해 입력 폴더와 출력 폴더를 지정해주세요.
input_folder_path_jpg = "./data_dataset_voc/JPEGImages"
output_folder_path_png = "./data_dataset_voc/PNGImages"

convert_all_jpg_to_png(input_folder_path_jpg, output_folder_path_png)