# -*- coding: utf8 -*-
from itertools import starmap, product, repeat
from pathlib import Path
import shutil
folder = 'X'


def sub_dir() -> map:
    return map(''.join, zip(repeat('a'), map(str, range(101))))


def main() -> None:
    for p in starmap(Path, product(folder, sub_dir(), 'st')):
        print(p)
        #shutil.rmtree(str(p))


def test_create_dir() -> None:
    for p in starmap(Path, product(folder, sub_dir(), 'stuv')):
        p.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    # テストのためのディレクトリ作成！
    #test_create_dir()
    main()
