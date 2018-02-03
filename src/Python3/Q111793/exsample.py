# -*- coding: utf8 -*-
from os import getpid
from time import sleep
from threading import current_thread
import concurrent.futures

import numpy as np


def 自作関数(引数1, 引数2):
    sleep(3)
    return f"pid={getpid()}, tid={current_thread().ident}, {引数1}, {引数2}"


def main():
    np.random.seed(42)
    test = np.random.random_integers(0, 500, 30)
    test2 = np.random.random_integers(0, 500, 30)
    assert len(test) == len(test2)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result, test in zip(executor.map(自作関数, test, test2), test):
            print(result)


if __name__ == '__main__':
    main()
