# -*- coding: utf-8 -*-
import csv
from datetime import datetime, timedelta
import os


def main():
    base_dir = os.path.dirname(__file__)
    now_time = datetime.today()
    with open(os.path.join(base_dir, 'xxxx.csv'), 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header = next(reader)
        row = header[0]
        file_time = datetime.strptime(row,  "%Y-%m-%d %H:%M:%S.%f")

    if abs(now_time - file_time) >= timedelta(minutes=3):
        print('YES')


if __name__ == '__main__':
    main()
