# -*- coding: utf-8 -*-
from tkinter import Tk, ttk, font, sys, messagebox


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("360x360")
        self.root.resizable(0, 0)
        self.root.title("BMIを計算してしまったのですが!")
        # self.root.iconbitmap("tehu.ico")
        font_ms = font.Font(family='MS ゴシック', size=24)

        weight = ttk.Label(self.root, text='体重:', font=font_ms)
        weight.place(x=30, y=60)
        height = ttk.Label(self.root, text='身長:', font=font_ms)
        height.place(x=30, y=150)
        BMI = ttk.Label(self.root, text='BMI:', font=font_ms)
        BMI.place(x=35, y=250)

        calc = ttk.Button(self.root, text='計算!', command=self.tehutehuapple)
        calc.place(x=145, y=200)
        end = ttk.Button(self.root, text='終了', command=sys.exit)
        end.place(x=145, y=330)

        self.weiBox = ttk.Entry()
        self.weiBox.place(x=120, y=70)
        self.heiBox = ttk.Entry()
        self.heiBox.place(x=120, y=160)

    def tehutehuapple(self):
        Wei = float(self.weiBox.get())
        Hei = float(self.heiBox.get())
        result = Wei / (Hei * Hei)
        BMIresult = ttk.Label(self.root, text=result)
        BMIresult.place(x=120, y=250)
        return

    def run(self):
        self.root.mainloop()
if __name__ == '__main__':
    app = App()
    app.run()
