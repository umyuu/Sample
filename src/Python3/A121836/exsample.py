# -*- coding: utf8 -*-
from contextlib import closing
import json
# pip install mysql-connector-python-rf
import mysql.connector


def connect():
    with open('settings.json', encoding='utf-8-sig') as f:
        json_data = json.load(f)
    con_str = json_data['connection_strings']
    print(con_str)
    return mysql.connector.connect(**con_str)


def main() -> None:
    with closing(connect()) as conn:
        with closing(conn.cursor()) as cur:
            for _ in cur.execute("create table sampleA (id int, rnd int);create table sampleB (id int, rnd int);", multi=True):
                pass
            conn.commit()


if __name__ == '__main__':
    main()
