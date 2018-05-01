# -*- coding: utf-8 -*-
from pathlib import Path


def main() ->None:
    base_path = Path('mainfld/subfld1')
    base_path.mkdir(parents=True, exist_ok=True)
    for i in range(1, 4):
        p = base_path / f'abc{i}.txt'
        with p.open('w') as f:
            pass


if __name__ == "__main__":
    main()
