# -*- coding: utf-8 -*-
import pandas as pd


def main():
    df = pd.read_csv('iris_data.txt', header=None)
    df.to_csv('iris_data_train.csv', header=False, index=False, columns=range(0, 4))
    df.to_csv('iris_target_train.csv', header=False, index=False, columns=range(4, 5))

if __name__ == '__main__':
    main()
