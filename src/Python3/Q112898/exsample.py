# -*- coding: utf8 -*-
import matplotlib.pyplot as plt


def main() -> None:
    source_Y1 = [['3', 'aaa'], ['2', 'bbb'], ['5', 'ccc'], ['4', 'ddd']]
    source_Y1.sort()
    print(source_Y1)
    Y1, X1 = map(list, zip(*source_Y1))
    print(X1)
    print(Y1)
    plt.bar(range(len(X1)), Y1, tick_label=X1, align="center")
    plt.show()


if __name__ == '__main__':
    main()
