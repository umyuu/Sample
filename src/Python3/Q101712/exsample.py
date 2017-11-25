# -*- coding: utf-8 -*-
import tkinter as Tk
from collections import OrderedDict
from pprint import PrettyPrinter


def load_widget():
    widget_list = list()
    widget_list.append({'type': 'Label', 'text': "Data File :", 'relx': 0.01, 'rely': 0.005})
    widget_list.append({'type': 'Entry', 'width': 80, 'relx': 0.07, 'rely': 0.01, 'focus_set': True})
    widget_list.append({'type': 'Label', 'text': "Ref File :", 'relx': 0.01, 'rely': 0.055})
    widget_list.append({'type': 'Entry', 'width': 80, 'relx': 0.07, 'rely': 0.055})
    widget_list.append({'type': 'Label', 'text': "Sample Name :", 'relx': 0.01, 'rely': 0.10})
    widget_list.append({'type': 'Entry', 'width': 20, 'relx': 0.1, 'rely': 0.105})
    return widget_list


def create_widgets(root):
    # ルート参照から到達できるように生成したwidgetを保持
    widget_dict = OrderedDict()
    for i, component in enumerate(load_widget()):
        widget = None
        if component['type'] == 'Label':
            widget = Tk.Label(root, text=component['text'])
        elif component['type'] == 'Entry':
            widget = Tk.Entry(root, width=component['width'])
            if 'focus_set' in component:
                if component['focus_set']:
                    widget.focus_set()
        else:
            assert widget is not None, component['type']
        widget.place(relx=component['relx'], rely=component['rely'])
        widget_dict[i] = widget
    return widget_dict


def main():
    root = Tk.Tk()
    root.geometry("1000x600")
    root.widgets = create_widgets(root)
    # 作成したwidgetを出力
    pp = PrettyPrinter(indent=4)
    pp.pprint(root.widgets)
    root.mainloop()


if __name__ == '__main__':
    main()
