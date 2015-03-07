#coding:utf-8
import wx

app=wx.App()

win=wx.Dialog(None,title='register',size=(400,280))
win.Center()

bgp=wx.Panel(win)

labelUsername=wx.StaticText(bgp,label='username:')
labelEmail=wx.StaticText(bgp,label='Email:')
labelPasswd=wx.StaticText(bgp,label='Password:')
labelConfirmPasswd=wx.StaticText(bgp,label='Confirme Password:')

textUsername=wx.TextCtrl(bgp)
textEmail=wx.TextCtrl(bgp)
textpassword=wx.TextCtrl(bgp)
textConfirmPassword=wx.TextCtrl(bgp)

btOK=wx.Button(bgp,label='Register')
topsizer=wx.FlexGridSizer(4,2,5,5)

topsizer.AddMany([(labelUsername,0,wx.ALIGN_RIGHT),(textUsername,1,wx.EXPAND|wx.RIGHT,10),
	(labelEmail,0,wx.ALIGN_RIGHT),(textEmail,1,wx.EXPAND|wx.RIGHT,10),
	(labelPasswd,0,wx.ALIGN_RIGHT),(textpassword,1,wx.EXPAND|wx.RIGHT,10),
	(labelConfirmPasswd,0,wx.ALIGN_RIGHT),(textConfirmPassword,1,wx.EXPAND|wx.RIGHT,10)])
topsizer.AddGrowableCol(1,1)


bottomBox=wx.BoxSizer(wx.VERTICAL)
bottomBox.Add(topsizer,1,wx.EXPAND|wx.TOP|wx.BOTTOM,40)
bottomBox.Add(btOK,1,wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, 30)

bgp.SetSizer(bottomBox)

win.Show()

app.MainLoop()