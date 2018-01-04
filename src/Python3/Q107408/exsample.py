# -*- coding: utf-8 -*-
import pandas as pd


def main():
    df = pd.DataFrame({"date": [20161208144911000, 20171208144911000, 20181208144911000],
                       "name": ['name1', 'name2', 'name3']
                       })

    df['out_date'] = pd.to_datetime(df['date'], format='%Y%m%d%H%M%S%f')
    df['year']= df['out_date'].dt.year
    df['month'] = df['out_date'].dt.month
    df['day'] = df['out_date'].dt.day
    df['hour'] = df['out_date'].dt.hour
    df['minute'] = df['out_date'].dt.minute
    df['second'] = df['out_date'].dt.second
    del df['out_date']
    print(df)


if __name__ == '__main__':
    main()
