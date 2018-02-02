#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import threading
from collections import OrderedDict
import functools
from tkinter import *
import tkinter.ttk as ttk

from selenium import webdriver


# メソッド名:task_runはあまり適切ではないかも！
def task_run(url):
    # webdriverをcloseしていないので、リソースリークに注意
    driver = webdriver.Chrome(r'C:\selenium\chromedriver')
    #driver = webdriver.Firefox()
    driver.get(url)


class Notebook(ttk.Notebook):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.style = ttk.Style()
        # tabメニューのpaddingを設定
        self.style.configure('TNotebook.Tab', padding=(10, 0, 10, 0))
        self.tab_pages = OrderedDict()
        self.create_widgets()

    def create_widgets(self):
        # rootコンポーネントのwidthとheigthを取得
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        self.tab_pages['tab_a'] = Frame(self, width=width, height=height)
        button_yahoo = Button(self.tab_pages['tab_a'],
                              command=functools.partial(Notebook.browser_open, 'https://www.yahoo.co.jp/'),
                              text='yahoo')
        button_yahoo.pack()

        self.tab_pages['tab_b'] = Frame(self, width=width, height=height)
        button_google = Button(self.tab_pages['tab_b'],
                               command=functools.partial(Notebook.browser_open, 'https://www.google.co.jp/'),
                               text='google')
        button_google.pack()
        for key, val in self.tab_pages.items():
            val.pack()
            # 登録されるtab名称(text)はOrderedDictのkey名
            self.add(val, text=key)
        self.pack(expand=True, fill=BOTH)

    @staticmethod
    def browser_open(url):
        # webdriverの生成に時間がかかり、イベントディスパッチスレッドがブロックするのを防ぐために別スレッドを生成する。
        thr = threading.Thread(target=task_run, args=(url,))
        thr.start()


def main():
    root = Tk()
    root.title(u"Software Title")
    root.geometry("400x300")
    root.update_idletasks()
    notebook = Notebook(root)
    root.mainloop()


if __name__ == '__main__':
    main()
