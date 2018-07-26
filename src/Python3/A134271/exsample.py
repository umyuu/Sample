import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("テストウィンドウ")
        self.geometry("640x480+1000+10")

        self.create_widgets()
        self.Bind()

    def create_widgets(self):
        #キャンバスの設定
        self.canvas = tk.Canvas(self, width = 300, height = 300)

        #画像の貼り付け
        self.img = Image.open('IMG/sample.png', 'r')
        self.rotate(0)
        self.canvas.place(x = 245, y = 100)

        self.testBtn = tk.Button(self, text="右に回転")
        self.testBtn.pack(anchor = tk.NW, side="top")

    def rotate(self, degrees:int):
        self.img = self.img.rotate(degrees, expand=True)
        self.photo = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, image=self.photo)

    def callback(self, evt):
        # ここで回転の処理を行いたい
        self.rotate(-90)

    def Bind(self):
        #テスト作成中
        self.testBtn.bind("<1>", self.callback)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()