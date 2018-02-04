# -*- coding: utf8 -*-
import sys
a = [[0, 0], [1, 1], [4, 2]]


def register_sublist_val(prefix: str, l: list) -> None:
    """
    list a => a1, a2, a3 , aN
    :param prefix:
    :param l:
    :return:
    """
    for i, val in enumerate(l):
        # 1 Origin
        key = prefix + str(i + 1)
        # 変数をモジュールスコープに追加
        setattr(sys.modules[__name__], key, val)


def main() -> None:
    register_sublist_val('a', a)
    print(a1)
    print(a2)
    print(a3)


if __name__ == '__main__':
    main()
