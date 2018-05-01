# -*- coding: utf8 -*-
from contextlib import closing
import json
# pip install PyMySQL
import pymysql
from pymysql.constants.CLIENT import MULTI_STATEMENTS


def connect():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='testdb',
                           client_flag=MULTI_STATEMENTS)


def main() -> None:
    with closing(connect()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute("select 1;create table sampleAAB (id int, rnd int);create table sampleBAA (id int, rnd int);")
            while True:
                print(cur.fetchall())
                if not cur.nextset():
                    break
            conn.commit()


if __name__ == '__main__':
    main()
