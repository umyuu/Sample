# -*- coding: utf8 -*-
import glob
import os
import pandas as pd
from pathlib import Path
import shutil


def move_files(base_dir: Path, file_path: list) ->None:

    for f in file_path:
        src = Path(f)
        print(src)
        # ※3
        df = pd.read_table(f, sep=",", encoding='utf-8-sig')
        # ※4
        dst_dir = Path(base_dir, df.loc[1, "name"])
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir.joinpath(src.name)
        # ファイルのメタデータを保持しつつコピー
        # shutil.copy2(str(src), str(dst))
        # ファイルを移動
        os.replace(str(src), str(dst))


def main() -> None:
    base_dir = Path("share_folder")
    # ※1
    file_path = glob.glob(str(base_dir.joinpath("*.txt")))
    if len(file_path) == 0:
        print(f'File Not Found:{base_dir}')
        return
    print(file_path)
    # ※2 ファイル一覧をソート！
    # file_path = sorted(file_path)
    move_files(base_dir, file_path)


if __name__ == '__main__':
    main()
