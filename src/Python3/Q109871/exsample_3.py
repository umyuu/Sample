# -*- coding: UTF-8 -*
import tkinter as Tk


# ↓追加
def set_window_visible(window, visible):
    if visible:
        window.deiconify()
    else:
        window.withdraw()
#

#Tk.Toplevelを継承するように変更
class VolumeWindow(Tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.f = Tk.Frame(self)
        self.f.pack()
        self.volume = Tk.IntVar()
        self.volume.set(50)
        self.volume_bar = Tk.Scale(self.f, orient='h',variable=self.volume)
        self.volume_bar.pack()
        set_window_visible(self, False)
        #VolumeWindowウィンドウを閉じる時のイベントを追加
        self.protocol('WM_DELETE_WINDOW', self.on_window_exit)

    def on_window_exit(self):
        # VolumeWindowウィンドウを閉じた時に呼ばれる処理
        # 親ウィンドウのボタンを活性化
        self.master.widgets_set_state(True)
        # ボリュームウィンドウを非表示に
        set_window_visible(self, False)


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
        set_window_visible(self.volume, True)
        self.widgets_set_state(False)

    def widgets_set_state(self, state):
        if state:
            self.volume_button.configure(state=Tk.NORMAL)
        else:
            self.volume_button.configure(state=Tk.DISABLED)


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
