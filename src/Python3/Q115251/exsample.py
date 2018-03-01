# -*- coding: utf8 -*-


def mufunc(end=25, multiple=2, non_multiple=5):
    for i in range(0, end + 1, multiple):
        if i % non_multiple:
            yield i


def main() -> None:
    for i in mufunc():
        print(i)


if __name__ == '__main__':
    main()
