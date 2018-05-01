# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from contextlib import closing
from threading import current_thread, get_ident
from time import sleep
from random import randint
import tkinter as tk


class MyFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.executor = ThreadPoolExecutor()
        self.pack()
        self.btn_task = tk.Button(self, text='task', command=self.task)
        self.btn_task.pack()

    def task(self):
        seconds = randint(0, 10)
        self.executor.submit(self.hardtask, seconds)

    def hardtask(self, seconds):
        print(f'tid:{get_ident()}, {current_thread().getName()}, {seconds}')
        sleep(seconds)

    def close(self):
        self.executor.shutdown(wait=False)


def main() ->None:
    root = tk.Tk()
    root.title("ThreadPoolExecutor")
    root.geometry("400x200")
    with closing(MyFrame(root)) as f:
        root.mainloop()


if __name__ == '__main__':
    main()
