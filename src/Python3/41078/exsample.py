# -*- coding: UTF-8 -*
from pathlib import Path
import cv2

import classfy01
from classfy02 import input_data2

def main():
    parent_path = Path(__file__).parent
    path = str(
        (parent_path / 'cross.png').resolve()
    )
    print(path)

    img = classfy01.imread(path)


if __name__ == '__main__':
    main()
