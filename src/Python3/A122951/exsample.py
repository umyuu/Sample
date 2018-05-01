# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
import os
from pathlib import Path
from threading import Thread
from time import sleep
#おまじない
import urllib #URLエンコード用
import bs4 #HTMl解析
import requests #URlアクセス？
import re #正規表現(URL抽出)
import tkinter as tk #GUI
#import ui #GUI作成


class MyFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack()

        # ロゴ？を表示
        # image1 = tk.PhotoImage(file = 'LOGO.gif')
        # tk.Label(frame1, image = image1).pack()#.grid(row=0, column=0)
        # ※検索キーワードのテキストボックスを作成
        self.key_word = tk.StringVar(value='草')
        self.txt_key_word = tk.Entry(self, textvariable=self.key_word)
        self.txt_key_word.pack()
        # 探すボタンを作成
        serch = tk.Button(self, text='探す', padx=45, pady=7, command=self.search)
        serch.pack()
        # 空白
        tk.Label(self, text="").pack()
        # オプションボタンを作成
        option = tk.Button(self, text='設定', padx=44, pady=7)  # 微調整しているため、padxの値がちょっとおかしい
        option.pack()
        # 空白
        tk.Label(self, text="").pack()
        # バグ連絡
        bug = tk.Button(self, text="バグ・要望等連絡", padx=15, pady=7)
        bug.pack()
        # 空白
        tk.Label(self, text="").pack()
        # 終了ボタンを作成
        owa = tk.Button(self, text="終了", padx=46, pady=7, command=self.owari)
        owa.pack()

    def search(self):
        search_word = self.key_word.get()
        # ※画面をブロックさせないためにスレッドを生成して、startを呼び出す。
        t = Thread(target=hack, args=(search_word,))
        t.start()

    def owari(self):
        quit()


class DownLoader(object):
    def __init__(self):
        # ミリ秒に変換
        self.interval = 500 / 1000
        # sec
        self.timeout = 10
        self.download_dir = Path('download')
        self.download_dir.mkdir(exist_ok=True)

    def get(self, url: str, params: dict=None):
        # 実際のリクエスト処理はここ
        res = requests.get(url, params=params, timeout=self.timeout)
        print(res.url)
        # http ステータスコードが200番台以外なら例外を発生させる。
        # 存在しないwebページをurlに指定すると例外が発生するので分かりやすいかと。
        res.raise_for_status()
        return res

    def get_content(self, url: str, params: dict=None):
        sleep(self.interval)
        res = self.get(url, params)
        return BytesIO(res.content), res.headers['content-type']

    def request(self, url_list: list) ->None:
        """
           internet -- (Get) --> local
           use ThreadPoolExecutor
        """
        count = 0
        with ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(self.get_content, url): url for url in url_list}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:

                    # get_contentの戻り値はここで取得
                    buffer, content_type = future.result()
                    # 保存対象のファイルかどうか。
                    if not self.save_content_type(content_type):
                        continue
                    # 保存ファイル名はURLのパス部分をそのまま取得
                    # 重複が発生するので連番を付けたりして対応してくださいな。
                    file_name = self.download_dir / os.path.basename(url)

                    print(content_type, file_name)
                    # 保存
                    self.save_file(buffer, file_name)
                    count += 1
                except Exception as ex:
                    print(f"url:{url}, {ex}")

        if count == 0:
            print(f'save file Empty')

    def save_content_type(self, content_type: str) ->bool:
        is_saved = ["image/jpeg", "image/png", "image/gif"]
        return content_type.lower() in is_saved

    def save_file(self, buffer: BytesIO, file_name: Path) ->None:
        with file_name.open('wb') as f:
            f.write(buffer.getvalue())


# ※Downloaderクラスのインスタンスを生成
dl = DownLoader()


#ダウンロード用(HTML)関数
def hack(search_word: str): #wordeで取得したURLから画像のURLを抜き出す(解析)　使用ライブラリ:bs4
    url = 'https://search.yahoo.co.jp/image/search'
    params = {'n': '60', 'p': search_word, 'search.x': '1'}
    res = dl.get(url, params)
    print(res.text)
    soup = bs4.BeautifulSoup(res.text, "html.parser") #わかんね
    elems = soup.select('a') #aタグを選択
    url_list = [] #URLを格納するリストやで
    for img in elems: #URL取得やで
        url_list.append(img.get('href'))
        #print (url_list)
    print(url_list)
    kazu = (len(url_list)) #判定

    #print (kazu)

    if kazu == 0: #URL数が0だった時、エラーを出す。
        error = "urlzeroerror"
        # ※即座に抜けて、if文のネストを減らす
        return
    tdo = url_list
    # ※リスト内の重複を削除
    url_list = list(set(url_list))
    # ※url_listの内容に対してリクエスト！
    dl.request(url_list)


def main() ->None:
    root = tk.Tk()
    # ウィンドウのタイトルを設定
    root.title("フリー画像ダウンローダ -ver1.0_beta")
    # ウィンドウの大きさを指定
    root.geometry("800x500")
    f = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()