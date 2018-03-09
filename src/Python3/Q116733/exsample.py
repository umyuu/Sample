# -*- coding: utf-8 -*-
import sqlite3
from contextlib import closing
from logging import FileHandler, DEBUG, getLogger

handler = FileHandler("test.log")
handler.setLevel(DEBUG)
logger = getLogger("test")
logger.setLevel(DEBUG)
logger.addHandler(handler)


def main() -> None:
    db_name = ':memory:'
    # connectionの閉じ忘れを防ぐためにcontextlib#closingを使用。
    with closing(sqlite3.connect(db_name)) as conn:
        conn.set_trace_callback(print)
        # ログ・ファイルにSQLを書き出したい時は以下のコメントを外してくださいな。
        #conn.set_trace_callback(logger.debug)
        conn.execute('SELECT 1')


if __name__ == "__main__":
    main()

