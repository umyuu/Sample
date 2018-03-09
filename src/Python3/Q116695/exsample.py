# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter

def date_generator():
    # 年,月,日,時間
    current_date = datetime(2006, 1, 1, 0)
    end_date = datetime(2006, 1, 1, 3)
    #end_date = datetime(2007, 1, 1, 0)
    while True:
        yield current_date
        current_date += timedelta(hours=1)
        if current_date == end_date:
            break


def main() -> None:
    not_founds = []
    file_sizes = Counter()
    for dt in date_generator():
        file_name = f"aaa_{dt.strftime('%Y%m%d%H')}.bin"
        p = Path(file_name)
        try:
            st_size = p.stat().st_size
            file_sizes[st_size] = str(p)
        except FileNotFoundError as ex:
            not_founds.append(str(p))
            pass
    # ファイルが存在しない物
    if len(not_founds) >0:
        print(not_founds)

    print(file_sizes.most_common(5))


if __name__ == "__main__":
    main()

