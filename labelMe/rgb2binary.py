import cv2
import os
import numpy as np

def replace_non_black_pixels(image_file_path, output_folder_path):
    # 출력 폴더가 없으면 생성
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 이미지 로드 (OpenCV는 BGR 순서로 채널을 읽습니다)
    image = cv2.imread(image_file_path)

    # 모든 검은색 픽셀을 마스크로 만듭니다
    black_pixels = (image == [0, 0, 0]).all(axis=-1)

    #image != [0, 0, 0]이 제대로 동작하지 않아 True와 False를 반전시킴.
    non_black_pixels = ~black_pixels

    # 마스크를 이용하여 검은색이 아닌 픽셀은 모두 흰색으로 변경합니다
    image[non_black_pixels] = [255, 255, 255]

    #RGB 3채널을 1채널로 변경
    grey_image = np.max(image, axis=2)

    # 변경된 이미지를 저장하거나 반환
    filePath = os.path.basename(image_file_path)
    file_name, extension = os.path.splitext(filePath)
    new_file_name = output_folder_path +"/"+ file_name + "_mask.png"
    cv2.imwrite(new_file_name, grey_image)


# 대상 폴더 경로 설정
input_folder_path = "./data_dataset_voc/SegmentationClassPNG"
output_folder_path = "./data_dataset_voc/SegmentationClassPNG_grey"

# 폴더 내 모든 파일 순회
for file_name in os.listdir(input_folder_path):
    image_file_path = os.path.join(input_folder_path, file_name)

    # 파일이 PNG 파일인 경우에만 변환 수행
    if image_file_path.lower().endswith(".png"):
        replace_non_black_pixels(image_file_path, output_folder_path)