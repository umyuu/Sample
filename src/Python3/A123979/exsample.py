# -*- coding: utf-8 -*-
import os
import cv2


def image_file_filter(file_name: str) -> bool:
    n = os.path.join("./face_scratch_image", file_name)
    return cv2.imread(n) is not None


img_file_name_list = os.listdir("./face_scratch_image/")
print(len(img_file_name_list))
img_file_name_list = list(filter(image_file_filter, img_file_name_list))
print(len(img_file_name_list))
print(img_file_name_list)

