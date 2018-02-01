#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import threading
from collections import OrderedDict
import functools
from tkinter import *
import tkinter.ttk as ttk
from selenium import webdriver


def task_run(url):
    # webdriverをcloseしていないので、リソースリークに注意
    driver = webdriver.Chrome(r'C:\selenium\chromedriver')
    #driver = webdriver.Firefox()
    driver.get(url)


class Notebook(ttk.Notebook):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.style = ttk.Style()
        # tabメニューのpadding設定
        self.style.configure('TNotebook.Tab', padding=(10, 0, 10, 0))
        self.tab_pages = OrderedDict()
        self.create_widgets()

    def create_widgets(self):
        self.tab_pages['a'] = Frame(self, width=400, height=200, name='a')
        button_yahoo = Button(self.tab_pages['a'],
                              command=functools.partial(self.browser_open, 'https://www.yahoo.co.jp/'),
                              text='yahoo')
        button_yahoo.pack()

        self.tab_pages['b'] = Frame(self, width=400, height=150, name='b')
        button_google = Button(self.tab_pages['b'],
                               command=functools.partial(self.browser_open, 'https://www.google.co.jp/'),
                               text='google')
        button_google.pack()
        for i, v in self.tab_pages.items():
            v.pack()
            self.add(v, text=i)
        self.pack(expand=True, fill=BOTH)

    def browser_open(self, url):
        # webdriverの生成に時間がかかり、イベントディスパッチスレッドがブロックするのを回避するために別スレッドを生成する。
        thr = threading.Thread(target=task_run, args=(url,))
        thr.start()


def main():
    root = Tk()
    root.title(u"Software Title")
    root.geometry("400x300")
    notebook = Notebook(root)
    root.mainloop()


if __name__ == '__main__':
    main()
