# -*- coding: utf8 -*-
from tkinter import *
from tkinter import ttk
import webbrowser


def urljump(event):
    widget = event.widget
    # 選択された要素のindexを取得
    index = int(widget.curselection()[0])
    url = widget.get(index)
    print(url)
    webbrowser.open_new(url)


def main() -> None:
    urls = ['https://www.google.co.jp', 'https://www.yahoo.co.jp/', 'https://www.amazon.co.jp/']

    root = Tk()
    root.title(u'Url Getter')
    root.geometry("300x300")

    frame = Frame(root)
    frame.grid()

    listbox1 = Listbox(frame, width=30, cursor="hand2")
    for url in urls:
        listbox1.insert(END, url)
    listbox1.bind("<<ListboxSelect>>", urljump)
    listbox1.grid(row=1, column=0)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox1.yview)
    listbox1['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=1, column=1)

    root.mainloop()


if __name__ == '__main__':
    main()
