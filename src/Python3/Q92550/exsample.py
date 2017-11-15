# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def main():
    df = pd.DataFrame([
        ['2011-09-10', -22.093712, 7.802341, 23.349343, -19.453997],
        ['2011-09-11', -22.136867, -5.215804, 7.802341, -6.501528],
        ['2011-09-12', -2.607902, 6.518480, -5.215804, 2.608242]
    ])
    df.columns = ['datetime', 'a', 'b', 'c', 'ClassLabel']
    print(df)

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df['ClassLabel'].values)
    cl = label_encoder.inverse_transform(y)

    print(y)
    # 実行結果
    # [0 1 2]

    print(cl)
    # 実行結果
    # [-19.453997  -6.501528   2.608242]


if __name__ == '__main__':
    main()
