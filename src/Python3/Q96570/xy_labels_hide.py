# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def image_save(file_name, data):
    """
    :param file_name: ファイル名
    :param data:データ　x, y
    :return:
    """
    assert isinstance(data, tuple)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    # x軸、y軸のラベルを非表示に
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)

    # 描画
    ax1.plot(*data)

    fig.savefig(file_name, bbox_inches='tight', pad_inches=0)


def main():
    x = np.arange(-4, 5, 0.1)
    y = np.sin(x)
    data = (x, y)
    image_save("graph.png", data)


if __name__ == '__main__':
    main()
