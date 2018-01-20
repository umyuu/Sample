# -*- coding: UTF-8 -*
from tkinter import ttk
from tkinter import *
import functools


class VolumeWindow(Toplevel):
    def __init__(self, root):
        super().__init__()
        # ウィンドウを閉じたときのイベントを登録
        self.protocol('WM_DELETE_WINDOW', functools.partial(self.on_window_exit, param=2))
        self.volumes = Scale(self, {'label': 'volume', 'from_': 0, 'to': 100,
                                    'length': 200, 'command': self.__on_changed_scale_value})
        self.volumes.pack()
        # 初期状態は非表示
        self.set_visible(False)

    def __on_changed_scale_value(self, event):
        # Scale(スライダ）を移動時にイベント発生
        pass

    def on_window_exit(self, param):
        # VolumeWindowウィンドウを閉じた時に呼ばれる処理
        if param == 2:
            self.set_visible(False)

    def set_visible(self, visible):
        # ウィンドウの表示を切り替える
        # visible:True 表示,False 非表示
        if visible:
            self.deiconify()
        else:
            self.withdraw()


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Q109871')
        # ウィンドウを閉じたときのイベントを登録
        self.root.protocol('WM_DELETE_WINDOW', functools.partial(self.on_window_exit, param=1))
        # ボリュームウィンドウを作成して、self.volume_windowに変数を保持
        self.volume_window = VolumeWindow(self.root)
        # ボタンクリック時はVolumeWindow#set_visibleをTrueで呼び出す。
        self.volume_button = Button(self.root, text='Volume',
                                       command=functools.partial(self.volume_window.set_visible, visible=True))
        self.volume_button.pack()

    def on_window_exit(self, param):
        # sys.exitを呼び出し。
        if param == 1:
            sys.exit(0)

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
