# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path


# JPGファイルのEXIF情報から撮影日時(DateTimeOriginal)情報を取得
def get_exif(img, field='DateTimeOriginal'):
    for k, v in img._getexif().items():
        if TAGS.get(k) == field:
            return v
    return None


def main():
    p = Path('photo.jpg')
    #画像ファイル読み込み
    with Image.open(p) as jpg_image:
        #EXIF情報を取得
        val = get_exif(jpg_image)
        # 2017:12:29 01:12:42 => 20171229
        val = val.replace(':', '')[:8]
        print('#' * 40)
        print(val)
        # EXIF情報を取得
        new_file = p.with_name(val).with_suffix(p.suffix)
        print('-' * 40)
        print(new_file)
    #↓のコメントを外すとファイルをリネーム
    #p.replace(new_file)


if __name__ == '__main__':
    main()
