# -*- coding: utf-8 -*-

#=========================================================================
# ライブラリ
#=========================================================================
# GUIを扱う
import tkinter as tk
# tkinterよりデザインが良くなる
from tkinter import ttk

#=========================================================================
# クラス定義
#=========================================================================
#-------------------------------------------------------------------------
# メインクラス (継承 : tk.Tk)
#-------------------------------------------------------------------------
class WordPracticeApp(tk.Tk):

    #---  コンストラクタ
    def __init__(self, *args, **kwargs):

        # 初期化
        tk.Tk.__init__(self, *args, **kwargs)

        # コンテナのフレームを生成
        container = tk.Frame(self)

        # コンテナ配置
        container.pack(side="top", fill="both", expand=True)

        # コンテナのグリッドを 1x1 にする
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # フレームを格納する配列
        self.frames = {}

        # ページを格納する配列
        pages = (
                    StartPage,
                    InputNamePage,
                    OptionSelectPage
                )

        # それぞれのページに対して
        for F in pages:
            # フレームを生成
            frame = F(container, self)

            # フレームを格納
            self.frames[F] = frame

            # フレームを配置
            frame.grid(row=0, column=0, sticky="nsew")


        # スタートページを表示
        self.show_frame(StartPage)


    #---  フレームを表示
    def show_frame(self, cont):

        # WordPracticeAppのcontのフレームを格納
        frame = self.frames[cont]

        # そのフレームを上位層へ
        frame.tkraise()


#-------------------------------------------------------------------------
# スタートページクラス (継承 : tk.Frame)
#-------------------------------------------------------------------------
class StartPage(tk.Frame):

    #---  コンストラクタ
    def __init__(self, parent, controller):

        # 初期化
        tk.Frame.__init__(self, parent)

        ### タイトル表示
        #--- ラベル生成
        # 空白
        spaceLabel1 = [tk.Label(self, text="") for column in range(10)]
        spaceLabel2 = [tk.Label(self, text="") for column in range(3)]
        # タイトル
        titleLabelFont  = ("Helevetice", 32, "bold")
        titleLabel      = ttk.Label(self,\
                                    text="WORDPRACTICE",\
                                    font=titleLabelFont)

        #--- ラベル配置
        # 空白
        for index in range(10):
            spaceLabel1[index].pack()
        # タイトル
        titleLabel.pack()

        ### ボタン表示
        #---  ボタン生成
        startButton =\
         ttk.Button( self, text="           Start           ",\
                     command=lambda : controller.show_frame(InputNamePage) )

        #---  ボタン配置
        # 空白
        for index in range(3):
            spaceLabel2[index].pack()
        # ボタン
        startButton.pack()



#-------------------------------------------------------------------------
# 名前入力ページクラス (継承 : tk.Frame)
#-------------------------------------------------------------------------
class InputNamePage(tk.Frame):

    #---  コンストラクタ
    def __init__(self, parent, controller):
        # 初期化
        tk.Frame.__init__(self, parent)

        ###  タイトル表示
        #---  ラベル生成
        #  空白
        spaceLabel1 = [tk.Label(self, text="") for column in range(5)]
        # タイトル
        titleLabelFont  = ("Helevetice", 18)
        titleLabel      =\
           ttk.Label(self,\
                     text="ユーザー名を入力してください。",\
                     font=titleLabelFont)

        #---  ラベル配置
        # 空白
        for index in range(5):
            spaceLabel1[index].pack()
        # タイトル
        titleLabel.pack()


        ### フレーム表示
        #---  フレーム生成
        frame = ttk.Frame(self)
        #---  フレーム配置
        frame.pack()


        ### ユーザー名入力表示
        #--- ラベル生成
        # 空白
        spaceLabel2 = [tk.Label(frame, text="") for column in range(3)]

        # ユーザー名
        userNameLabelFont  = ("Helevetice", 14)
        userNameLabel      =\
          ttk.Label(frame, text="ユーザー名：", font=userNameLabelFont)

        #--- ラベル配置
        # 空白
        for index in range(3):
            spaceLabel2[index].grid(row=index, column=0)
        # ユーザー名
        userNameLabel.grid(row=4, column=0)

        #---  エントリー生成
        userName = tk.StringVar()
        userNameEntry = ttk.Entry(frame, textvariable=userName, width=30)

        #---  エントリー配置
        userNameEntry.grid(row=4, column=1)


        ### ボタン表示
        #---  ボタン生成
        okButton = ttk.Button( frame, text="  OK  ",\
                               command=lambda :\
                               controller.show_frame(OptionSelectPage) )

        #---  ボタン配置
        okButton.grid(row=4, column=3)


#-------------------------------------------------------------------------
# 問題形式選択ページクラス (継承 : tk.Frame)
#-------------------------------------------------------------------------
class OptionSelectPage(tk.Frame):

    #---  コンストラクタ
    def __init__(self, parent, controller):

        # 初期化
        tk.Frame.__init__(self, parent)

        ###  タイトル表示
        #---  ラベル生成
        #  空白
        spaceLabel1 = [tk.Label(self, text="") for column in range(5)]
        # タイトル
        titleLabelFont  = ("Helevetice", 18)
        titleLabel      =\
           ttk.Label(self,\
                     text="問題形式を選択してください。",\
                     font=titleLabelFont)

        #---  ラベル配置
        # 空白
        for index in range(5):
            spaceLabel1[index].pack()
        # タイトル
        titleLabel.pack()



#=========================================================================
# 本体処理
#=========================================================================
application = WordPracticeApp()
application.mainloop()