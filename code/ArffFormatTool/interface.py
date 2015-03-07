#coding:utf-8
import wx

from excel_to_arff import Switch

class FileDrop(wx.FileDropTarget):
	def __init__(self,window):
		wx.FileDropTarget.__init__(self)
		self.window=window

	def OnDropFiles(self,x,y,filenames):
		self.window.SetValue(str(filenames).split("'")[1])

class TransInterface(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self,None)
        self.Center()
        self.mainPanel()
        self.Show()

    def mainPanel(self):
        bgp=wx.Panel(self)
        
        self.source=wx.TextCtrl(bgp,size=(220,25))
        dropText=FileDrop(self.source)
        self.source.SetDropTarget(dropText)
        label1=wx.StaticText(bgp,label='source file name:')
        
        self.target=wx.TextCtrl(bgp,size=(220,25))
        label2=wx.StaticText(bgp,label='target file name:')
        
        self.ok=wx.Button(bgp,label='transformate')
        self.ok.Bind(wx.EVT_BUTTON,self.doTransfer)
        someHelp=wx.StaticText(bgp,label='need help?')

        top=wx.FlexGridSizer(3,2,10,10)
        top.Add(label1)
        top.Add(self.source)
        top.Add(label2)
        top.Add(self.target)
        top.Add(someHelp,wx.ALIGN_LEFT)
        fill=wx.BoxSizer()
        fill.Add(wx.StaticText(bgp,label=''),1,wx.EXPAND)
        fill.Add(self.ok,0,wx.ALIGN_RIGHT)
        top.Add(fill,1,wx.EXPAND)

        mBox=wx.BoxSizer()
        mBox.Add(top,1,wx.EXPAND|wx.ALL|wx.ALIGN_CENTER,border=10)
        
        bgp.SetSizer(mBox)

    def doTransfer(self,evt):
        fromSource=self.source.GetValue()
        toTarget=self.target.GetValue()
        if not(toTarget.split('\\')[-1].split('.')[-1]=='arff'):
            toTarget=toTarget+'.arff'
        tran = Switch(fromSource,toTarget)
        tran.trans()

if __name__=='__main__':
    app=wx.App()
    a=TransInterface()
    app.MainLoop()
