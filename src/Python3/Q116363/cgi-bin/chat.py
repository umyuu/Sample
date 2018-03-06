# -*- coding: utf-8 -*-
import cgi
import cgitb
import os.path
from pathlib import Path
import html

# ブラウザーでのデバックを有効にする
cgitb.enable()

# 全体の設定
FILE_LOG = "chat-log.txt"


def print_html(body: str) ->None:
    # HTMLを画面に表示する
    # ヘッダーを出力
    print("Content-Type: text/html; charset=utf-8")
    print("")
    # HTMLを出力
    print("""
    <html><head><meta charset="utf-8">
    <title>チャット</title></head><body>
    <h1>チャット</h1>
    <div><form>
    名前 : <input type="text" name="name" size ="8">
    本文 : <input type="text" name="body" size ="20">
    <input type="submit" value="発言">
    <input type="hidden" name="mode" value="write">
    </form></div><hr>
    {0}
    </body></html>
        """.format(body))


def mode_read(form) ->None:
    # チャットに書き込みログを表示する
    # ログを読み取る
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding="utf-8-sig") as f:
            log = f.read()
    print_html(log)


def jump(url: str) ->None:
    # 任意のURLにジャンプする
    # ヘッダー出力
    print("status: 301 Moved permanently")
    print("Location:" + url)
    print("")
    # HTMLを出力（ヘッダーがうまくいかなかった時の対策）
    print('<html><head>')
    print('<meta http-equiv="refresh" content="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">jump</a></body></html>')


def mode_write(form) ->None:
    # メッセージの書き込み
    # パラメーターの取得
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    # HTMLに変換
    name = html.escape(name)
    body = html.escape(body)
    # ファイルに保存
    with open(FILE_LOG, "a+", encoding='utf-8-sig') as f:
        f.write("<p>{0}:{1}</p><hr>\n".format(name, body))
    # 書き込み後にリダイレクト
    jump(Path(__file__).name)


# メイン処理
def main() ->None:
    # フォームの値を取得
    form = cgi.FieldStorage()
    # modeパラメータを取得
    mode = form.getvalue("mode", "read")
    if mode == "write":
        mode_write(form)
    else:
        mode_read(form)


if __name__ == "__main__":
    main()