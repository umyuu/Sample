# -*- coding: UTF-8 -*
from tkinter import *
# ※１　上記行と同じ事をしているためコメントアウト
# import tkinter
import PIL.Image
import PIL.ImageTk
import os
import functools
from collections import Counter
# import pygame
# import re, sys
# フレーム速度 [ms]
TIME = 33
# ※２_settingの処理時間計測用
times = Counter()


def on_application_exit(param):
    # ※３　終了処理はexitを呼び出し！
    sys.exit(0)

# ※４　Frame→Toplevelに変更
class App(Toplevel):
    # startedは再生しているかどうかを保持
    started = False
    # ※５ viewerの参照を保持
    viewers = []

    def __init__(self, master, path=''):
        super().__init__()
        App.viewers.append(self)
        # ※６　ウィンドウを閉じたときの終了イベントを追加
        self.protocol('WM_DELETE_WINDOW', functools.partial(on_application_exit, param=1))
        # ディクレクトリ内のファイルのリストを取得する
        self.image_path = path

        self.ls = os.listdir(path)
        # ※７　listdirではファイルの取得順序は保証されていない！のでソート処理を追加
        self.ls = sorted(self.ls)
        # ディクレクトリ内のファイルリストで余分なファイルを削除
        # b = self.ls.remove(os.path.basename(__file__))

        # ※８　Progressクラスを新規追加し、進捗を管理
        class Progress(object):
            def __init__(self, maximum=0):
                self.minimum = 0
                self.maximum = maximum
                self.value = 0

            def perform_step(self):
                if self.maximum == self.value:
                    return
                self.value += 1

            def reset(self):
                self.value = self.minimum
        self.progress = Progress(len(self.ls))
        # ラベルの設定
        self.la = Label(self)
        self.la.pack()
        #※９　self.packをコメントアウト
        #self.pack()
        self.bind_all('<1>', App.viewer_click)
        self.bind_all('<3>', App.all_reset)
        self._setting()

    def reset(self, event):
        self.progress.reset()
        self._setting()

    def next_image(self):
        if not self.started:
            return
        self.progress.perform_step()
        if self.progress.value < self.progress.maximum:
            self._setting()
        else:
            self.reset(None)

    def _setting(self):
        # ※１０　time.perf_counter()で計測すると_setting内の処理時間が30fpsを余裕でオーバーしている
        import time
        start = time.perf_counter()
        # 画像を読み込み、タイトルを変える
        filename = self.image_path + self.ls[self.progress.value]
        img = PIL.Image.open(filename)
        self.image = PIL.ImageTk.PhotoImage(img)
        elapsed_time = time.perf_counter() - start
        # ※２
        times[round(elapsed_time * 1000, 3)] += 1
        self.la.configure(image=self.image)
        self.title(os.path.basename(filename))

    @staticmethod
    def viewer_click(event):
        # マウスクリックでスタートとストップを切り替える
        App.started = not App.started
        if App.started:
            image_update()
            return

    @staticmethod
    def all_reset(event):
        for app in App.viewers:
            app.reset(event)


def image_update():
    for app in App.viewers:
        app.next_image()
    if App.started:
        root.after(TIME, decorated)


root = Tk()
decorated = functools.update_wrapper(functools.partial(image_update), image_update)


def main():
    # ※１１　root windowを非表示
    root.withdraw()
    root.protocol('WM_DELETE_WINDOW', functools.partial(on_application_exit, param=0))
    viewer_params = [
        {'path': './src/img/0/', 'x': 50, 'y': 50},
        {'path': './src/img/1/', 'x': 50, 'y': 460},
        {'path': './src/img/2/', 'x': 460, 'y': 50},
        {'path': './src/img/3/', 'x': 460, 'y': 460}
    ]
    for para in viewer_params:
        app = App(root, para['path'])
        # ※１２ 他のwindowとの位置をgeometryで設定
        # geometry width*height+x+y
        app.geometry("{0}x{1}+{2}+{3}".format(400, 400, para['x'], para['y']))
    root.mainloop()


if __name__ == '__main__':
    main()
