# -*- coding: utf-8 -*-
from pathlib import Path

import cv2
import math
import numpy as np


def while_color_mask():
    sensitivity = 45
    lower = np.array([0, 0, 255 - sensitivity])
    upper = np.array([255, sensitivity, 255])
    return lower, upper


def main():
    file_name = str(Path(__file__).parent / "image.jpeg")
    img_src = cv2.imread(file_name)
    # ※cv2.imreadの戻り値は絶対にチェックすること。
    assert img_src is not None, file_name

    hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)
    white = cv2.inRange(hsv, *while_color_mask())
    drop_img = cv2.bitwise_and(img_src, img_src, mask=white)
    cv2.imshow('drop_img', drop_img)

    # 入力画像をグレースケール変換
    gray = cv2.cvtColor(drop_img, cv2.COLOR_BGR2GRAY)

    # LSD生成
    LSD = cv2.createLineSegmentDetector()

    # 線分検出
    lines, width, prec, nfa = LSD.detect(gray)

    # グレースケール変換をBGR変換
    color = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # 直線の描画

    for pos in lines:
        for x1, y1, x2, y2 in pos:
            cv2.line(color, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # OpenCVがBGRなのでRGBに変換
    disp_in_img = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

    cv2.imshow('src', img_src)
    cv2.imshow('dst', disp_in_img)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()