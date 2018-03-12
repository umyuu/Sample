# -*- coding: utf-8 -*-
import sys
import tkinter


def main() -> None:
    # GUI設定
    root = tkinter.Tk()
    root.title(u"Software Title")
    root.geometry("400x300")

    # ラベル
    Static1 = tkinter.Label(text=u'test')
    Static1.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
