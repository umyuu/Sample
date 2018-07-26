# -*- coding: utf-8 -*-
import wx
import os
from functools import partial

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'logplot')
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour(wx.Colour(128, 128, 128))

        #button
        button_1 = wx.ToggleButton(panel, wx.ID_ANY, 'Line/Log')
        button_1.Bind(wx.EVT_TOGGLEBUTTON, self.button_click)

        # comboboxとbuttonの宣言順を変えている点に注意
        #combobox
        combobox_1 = wx.ComboBox(panel, wx.ID_ANY, 'select ScanList', choices = ("1","2","3"), style = wx.CB_READONLY)
        combobox_1.Bind(wx.EVT_TEXT, partial(self.Ontext, btn=button_1))

        #Text
        text_1 = wx.StaticText(panel, wx.ID_ANY, )

        vbox_1 = wx.BoxSizer(wx.VERTICAL)
        vbox_1.Add(combobox_1, 0, wx.LEFT | wx.RIGHT, 10)
        vbox_1.Add(button_1, 0, wx.RIGHT, 10)
        vbox_1.Add(text_1, 0, wx.RIGHT, 10)

        panel.SetSizer(vbox_1)

    def button_click(self, event):
        button_1 = event.GetEventObject()
        if button_1.GetValue():
            button_1.SetLabel("Log")
        else:
            button_1.SetLabel("Line")
        print(button_1.GetValue())

    def Ontext(self, event, btn):
        print(btn.GetValue())
        combobox_1 = event.GetEventObject()
        print(combobox_1.GetValue())


#モジュール空間の汚染を避けるためにスコープを切る
def main() -> None:
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
