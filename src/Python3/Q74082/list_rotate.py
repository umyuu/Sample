# -*- coding: utf-8 -*-
from collections import deque


def main():
    n = int(input())  # ずらす個数
    code = [1, 2, 3, 4]
    items = deque(code)
    print(items)
    items.rotate(n * -1)
    print(items)
    # dequeからlistに戻す
    code = list(items)
    print(code)
def test():
    n = int(input())  # ずらす個数
    code = [1, 2, 3, 4]
    memo = code
    for i in range(4):
        code[i] = memo[(i + n) % 4]  # nだけ配列のインデクスを右にずらしたい
    print(memo)  # => [2, 3, 4, 2] 3番目がうまくいかない
    print(code)  # => [2, 3, 4, 2]

if __name__ == '__main__':
    main()
    #test()