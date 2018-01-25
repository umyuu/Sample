# -*- coding: UTF-8 -*
from itertools import filterfalse


def main():
    data_text = ['', 0, None]
    print(data_text)
    filtered = list(filterfalse(lambda x: x is None, data_text))
    print(filtered)


if __name__ == "__main__":
    main()
