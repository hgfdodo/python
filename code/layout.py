#coding:utf-8

import wx
app=wx.App()
win=wx.Frame(None,title='editor',size=(410,340))

def openFile(evt):
	print evt
	print str(evt)
	filepath = path.GetValue()
	try:
		f=open(filepath)
		contents.SetValue(f.read())
		f.close()
	except Exception,e:
		contents.SetValue(str(e))

def saveFile(evt):
	filepath=path.GetValue()
	try:
		f=open(filepath,'w')
		f.write(contents.GetValue())
		f.flush()
		f.close()
		wx.MessageBox("write OK!")
	except Exception,e:
		contents.SetValue(str(e))

bgp=wx.Panel(win)

path=wx.TextCtrl(bgp)
btOpen=wx.Button(bgp,label='OPEN')
btSave=wx.Button(bgp,label='SAVE')
contents=wx.TextCtrl(bgp,style=wx.TE_MULTILINE|wx.HSCROLL)

btOpen.Bind(wx.EVT_BUTTON, openFile)
btSave.Bind(wx.EVT_BUTTON, saveFile)

topBox=wx.BoxSizer()
topBox.Add(path,proportion=1,flag=wx.EXPAND)
topBox.Add(btOpen,proportion=0,flag=wx.LEFT,border=5)
topBox.Add(btSave,proportion=0,flag=wx.LEFT,border=5)

bottomBox=wx.BoxSizer(wx.VERTICAL)
bottomBox.Add(topBox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
bottomBox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)


bgp.SetSizer(bottomBox)

win.Show()
app.MainLoop()