from tkinter import *
from tkinter import ttk
from random import choice


class Word(object):
    def __init__(self):
        self.when_list = ['今日', '明日']
        self.where_list = ['東京', '埼玉']
        self.who_list = ['私', 'あなた']
        self.with_who = ['東京', '埼玉']
        self.how_list = ['東京', '埼玉']
        self.do_list = ['東京', '埼玉']

    def get4WHD(self):
        yield choice(self.when_list)
        yield choice(self.where_list)
        yield choice(self.who_list)
        yield choice(self.with_who)
        yield choice(self.how_list)
        yield choice(self.do_list)



class MyFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, height=300, width=500)
        self.grid()
        self.word = Word()

        # プログラムの題名みたいなのを描写する用ののラベル
        self.label_title = ttk.Label(
            root,
            text="「　いつどこでだれがだれとどのようになにをした　」",
            background=("#ffffff"),
            padding=(50, 5)
        )
        self.label_title.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

        # 「いつ」という文字を表示するようのラベル
        self.label_when = ttk.Label(
            root,
            text="いつ",
            background=("#ffff00"),
            padding=(50, 5)
        )
        self.label_when.grid(row=1, column=0, padx=10, pady=10)

        # 「どこで」という文字を表示するようのラベル
        self.label_where = ttk.Label(
            root,
            text="どこで",
            background=("#1e90ff"),
            padding=(50, 5)
        )
        self.label_where.grid(row=1, column=1, padx=10, pady=10)

        # 「だれが」という文字を表示するようのラベル
        self.label_who = ttk.Label(
            root,
            text="だれが",
            background=("#adff2f"),
            padding=(50, 5)
        )
        self.label_who.grid(row=1, column=2, padx=10, pady=10)

        # 「だれと」という文字を表示するようのラベル
        self.label_with = ttk.Label(
            root,
            text="だれと",
            background=("#f08080"),
            padding=(50, 5)
        )
        self.label_with.grid(row=1, column=3, padx=10, pady=10)

        # 「どのように」という文字を表示するようのラベル
        self.label_how = ttk.Label(
            root,
            text="どのように",
            background=("#ffa500"),
            padding=(50, 5)
        )
        self.label_how.grid(row=1, column=4, padx=10, pady=10)

        # 「なにをした」という文字を表示するようのラベル
        self.label_do = ttk.Label(
            root,
            text="なにをした",
            background=("#da70d6"),
            padding=(50, 5)
        )
        self.label_do.grid(row=1, column=5, padx=10, pady=10)
        # 結果を表示するよう
        self.label_answer = (ttk.Label(root), ttk.Label(root), ttk.Label(root),
                        ttk.Label(root), ttk.Label(root), ttk.Label(root))
        for i, l in enumerate(self.label_answer):
            l.configure(background=("#ffffff"),padding=(50, 5),relief="ridge")
            l.grid(row=2, column=i, padx=10, pady=10)
        self.set_answer()

        self.button1 = ttk.Button(
            self, text="OK?",padding=(50, 5),command=self.buttonClick)
        self.button1.grid(row=3, column=0, padx=10, pady=10, columnspan=6)

    def set_answer(self):
        for i, v in enumerate(self.word.get4WHD()):
            self.label_answer[i].configure(text=v)

    def buttonClick(self):
        self.set_answer()


def main() ->None:
    root = Tk()
    root.title("いつどこで・・・")
    f = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()