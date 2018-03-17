# -*- coding: utf-8 -*-
import random


def main() -> None:
    dic = {1: 'a', 2: 'b', 3: 'c', 4: 'c'}
    print(random.sample(list(dic), len(dic)))


if __name__ == "__main__":
    main()

