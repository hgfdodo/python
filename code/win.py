import wx
#coding:utf-8

app=wx.App()
win=wx.Frame(None,title="editor",size=(410,335))
buttonOpen=wx.Button(win,label='open',pos=(230,0),size=(80,25))
buttonClose=wx.Button(win,label='save',pos=(315,0),size=(80,25))

filename=wx.TextCtrl(win,pos=(0,0),size=(225,25))

editor=wx.TextCtrl(win,pos=(0,30),size=(395,270),style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL)

win.Show()
app.MainLoop()
