# -*- coding: utf8 -*-
import csv
from contextlib import closing
import json
import random
# pip install mysql-connector-python-rf
import mysql.connector

# MySQLのDB名:testdbにデータを登録するサンプルです。


def connect():
    with open('settings.json', encoding='utf-8-sig') as f:
        json_data = json.load(f)
    con_str = json_data['connection_strings']
    print(con_str)
    return mysql.connector.connect(**con_str)


def read_csv(file_name: str='data.csv', encoding='utf-8-sig'):
    with open(file_name, encoding=encoding) as csv_file:
        reader = csv.reader(csv_file)
        # ↓ヘッダー行のスキップを行いたい時
        #next(reader)
        yield from reader


def insert_data(cur) -> int:
    random.seed(42)
    row_count = 0
    sql = f"insert into sample (id, rnd, item, qty) values (%s, %s, %s, %s)"
    for i, rows in enumerate(read_csv()):
        print(*rows)
        rnd = random.randint(0, 500)
        item = rows[0]
        qty = rows[1]
        params = (i, rnd, item, qty)
        cur.execute(sql, params)
        row_count += cur.rowcount

    print(f"rowcount:{row_count}")
    return row_count


def select_data(cur) -> None:
    sql = f"SELECT * FROM sample ORDER BY id"
    print("#" * 40)
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)


def main() -> None:
    with closing(connect()) as conn:
        conn.ping(reconnect=True)
        with closing(conn.cursor()) as cur:
            # drop table
            cur.execute(f"drop table if exists sample")
            # create table
            cur.execute(f"create table sample (id int, rnd int, item TEXT, qty int)")
            # insert
            insert_data(cur)
            # select
            select_data(cur)
            # データベースへの変更を確定
            conn.commit()


if __name__ == '__main__':
    main()
