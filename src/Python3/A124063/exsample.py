# -*- coding: utf-8 -*-
from contextlib import closing
import sqlite3


def is_exists(one_row: tuple) ->bool:
    # ブール演算子 and, or, notはショートカットサーキット演算子です。
    # https://docs.python.jp/3/reference/expressions.html#boolean-operations
    return one_row is not None and len(one_row) != 0


def main() ->None:
    # データベースのclose忘れを防ぐために、contextlib#closingを使用
    with closing(sqlite3.connect("userInfo.db")) as con:
        # 実行SQLをprint文で出力
        con.set_trace_callback(print)
        cur = con.cursor()

        userName1 = "aaaaa"
        userName2 = "bbbbb"
        # 1,SQLインジェクションを防止するために、bindパラメータを使用
        # 2,SQLの実行エラー対応 2-1,form→from、2-2,whereで列名を指定
        # 3,ORDER BY句を指定して、結果の並び順を保証するように変更
        cur.execute('select * from users where userName =? order by id', (userName1,))
        tuple1 = cur.fetchone()

        cur.execute('select * from users where userName =? order by id', (userName2,))
        tuple2 = cur.fetchone()

        if is_exists(tuple2):
            print("OK")
        else:
            print("NO")


if __name__ == "__main__":
    main()
