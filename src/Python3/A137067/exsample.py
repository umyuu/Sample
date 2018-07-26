# -*- coding: utf-8 -*-
import wx 


class ChildFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,wx.ID_ANY,"child frame",pos=(100,100))

        pane2 = wx.Panel(self)
        self.exitBtn = wx.Button(pane2,label="閉じる",pos=(100,10))
        self.Bind(wx.EVT_BUTTON,self.exit2,self.exitBtn)

    def exit2(self,event):
        # 画面を閉じるではなく非表示に
        self.Show(False)

class MyWindow(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,wx.ID_ANY,"main frame")
        panel = wx.Panel(self)
        self.showChildBtn = wx.Button(panel,label="show child",pos=(10,10))
        self.exitBtn = wx.Button(panel,label="exit",pos=(100,10))
        self.Bind(wx.EVT_BUTTON,self.showChild,self.showChildBtn)
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)
        # 子画面を生成する
        self.childFrame = ChildFrame(self)

    def showChild(self,event):
        childID = self.childFrame.Show()
        return True

    def exit(self, event):
        childFrame = ChildFrame(self)
        # 上記で作った子画面を閉じる
        childFrame.Show(True)
        #childFrame.Close(True)
        self.childFrame.exit2(None)



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyWindow(parent=None,id=wx.ID_ANY)
    frame.Show()
    app.MainLoop()




