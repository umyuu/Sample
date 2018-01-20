# -*- coding: UTF-8 -*
import tkinter as Tk


# ↓追加　ここから
def set_window_visible(window, visible):
    if visible:
        window.deiconify()
    else:
        window.withdraw()
# ↑追加　ここまで


class VolumeWindow:

    def __init__(self, master):
        # masterはFrame型
        self.master = master
        self.top = Tk.Toplevel(self.master)
        self.f = Tk.Frame(self.top)
        self.f.pack()
        self.volume = Tk.IntVar()
        self.volume.set(50)
        self.volume_bar = Tk.Scale(self.f, orient='h',variable=self.volume)
        self.volume_bar.pack()
        set_window_visible(self.top, False)
        #VolumeWindowウィンドウを閉じる時のイベントを追加
        self.top.protocol('WM_DELETE_WINDOW', self.on_window_exit)

    def on_window_exit(self):
        # VolumeWindowウィンドウを閉じた時に呼ばれる処理
        # Frame型の変数volume_buttonを設定
        self.master.volume_button.configure(state=Tk.NORMAL)
        # ボリュームウィンドウを非表示に
        set_window_visible(self.top, False)


class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.f = Tk.Frame(self)
        self.f.pack()
        # 引数をFrameに変更
        self.volume = VolumeWindow(self)
        self.f_button = Tk.Frame(self.f)
        self.f_button.pack()
        self.volume_button = Tk.Button(self.f_button, text='Volume', command=self.control_volume, state=Tk.NORMAL)
        self.volume_button.pack(padx=5, pady=5, side=Tk.LEFT)

    def control_volume(self):
        # make_windowはしない。ボリュームウィンドウを表示するだけ。
        #self.volume.make_window()
        set_window_visible(self.volume.top, True)
        self.volume_button.configure(state=Tk.DISABLED)


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
