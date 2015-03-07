#coding:utf-8
import wx

app=wx.App()
win=wx.Dialog(None,title='login',size=(320,180))
win.Center()

labelUser = wx.StaticText(win,label="username:",pos=(25,30))
textUsername=wx.TextCtrl(win,pos=(100,30),size=(150,25))
labelPasswd = wx.StaticText(win,label="password:",pos=(25,70))
textpasswd=wx.TextCtrl(win,pos=(100,70),size=(150,25))
btLogin=wx.Button(win,label='Login',pos=(200,120),size=(80,25))

win.Show()
app.MainLoop()