# -*- coding: UTF-8 -*
from tkinter import ttk
from tkinter import *


def show_selection(lb, label):
    for i in lb.curselection():
        value = lb.get(i)
        label.config(text=value)
        break


def main():
    root = Tk()
    root.title('Scrollbar 1')

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # Listbox
    currencies = ("A", "B")
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=3)
    lb.grid(row=0, column=0)

    # Label (新規追加)
    label = Label(frame1, width=18)
    label.grid(row=1, column=0, columnspan=2)

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=1,sticky=(N,S))
    #Button
    button1 = ttk.Button(frame1, text='OK', command=lambda: show_selection(lb, label))
    button1.grid(row=6, column=0, columnspan=2)

    root.mainloop()


if __name__ == '__main__':
    main()
