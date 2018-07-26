# -*- coding: utf-8 -*-
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fileread():
    file_name = BASE_DIR / 'x.dat'
    with file_name.open('r') as f:
        while True:
            c = f.read(1)
            if c == '':
                break
            yield c


def main() -> None:
    file_name = BASE_DIR / 'output.dat'
    with file_name.open('w') as out:
        for c in fileread():
            out.write(c)
            out.write('\n')


if __name__ == "__main__":
    main()
