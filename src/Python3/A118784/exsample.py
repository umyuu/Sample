# -*- coding: utf8 -*-
import sqlite3
from contextlib import closing

tablename = 'sample'


def insert_data(cur: sqlite3.Cursor) -> int:
    import random
    random.seed(42)
    row_count = 0
    for i in range(10):
        sql = f"insert into {tablename} values (?, ?)"
        params = (i, random.randint(0, 500))
        cur.execute(sql, params)
        row_count += cur.rowcount

    print(f"rowcount:{row_count}")
    return row_count


def select_data(cur: sqlite3.Cursor) -> None:
    sql = f"SELECT * FROM {tablename} ORDER BY id"

    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("#" * 40)
    for row in rows:
        print(row)


def main() -> None:
    db_name = 'sample.db'
    with closing(sqlite3.connect(db_name)) as conn:
        conn.set_trace_callback(print)
        cur = conn.cursor()
        cur.execute(f"drop table if exists {tablename}")
        cur.execute(f"create table {tablename} (id, rnd)")
        insert_data(cur)
        select_data(cur)
        # コミット忘れに注意！
        conn.commit()


if __name__ == '__main__':
    main()
