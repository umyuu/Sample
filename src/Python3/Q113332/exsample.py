# -*- coding: utf8 -*-
import sqlite3
from contextlib import closing

tablename = 'sample'


def drop_table(cur: sqlite3.Cursor) -> None:
    sql = f"drop table if exists {tablename}"
    print(sql)
    cur.execute(sql)


def create_table(cur: sqlite3.Cursor) -> None:
    column名 = 'id, rnd'
    # f文字列を使う
    sql = f"create table {tablename} ({column名})"
    print(sql)
    cur.execute(sql)


def insert_data(cur: sqlite3.Cursor) -> None:
    import random
    random.seed(42)
    row_count = 0
    for i in range(10):
        sql = f"insert into {tablename} values (?, ?)"
        # bindパラメータを使用する tupleである点に注意
        params = (i, random.randint(0, 500))
        cur.execute(sql, params)
        row_count += cur.rowcount

    print(f"rowcount:{row_count}")


def select_data(cur: sqlite3.Cursor) -> None:
    sql = f"SELECT * FROM {tablename} ORDER BY id"
    print(sql)
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)


def main() -> None:
    db_name = 'database.db'
    with closing(sqlite3.connect(db_name)) as conn:
        cur = conn.cursor()
        drop_table(cur)
        create_table(cur)
        insert_data(cur)
        select_data(cur)
        # コミット忘れに注意！
        conn.commit()


if __name__ == '__main__':
    main()
