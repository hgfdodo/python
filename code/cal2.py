import wx
import math

class Calculation(wx.Frame):
	__result=0
	__fu=''
	__qian=0
	__hou=0
	def __init__(self):
		self.app=wx.App()
		wx.Frame.__init__(self,None,size=(600,150))
		self.Center()
		self.__fun()
		self.Show()
		self.app.MainLoop()

	def __fun(self):
		bgp=wx.Panel(self)

		self.qian=wx.TextCtrl(bgp,size=(120,25))
		self.hou=wx.TextCtrl(bgp,size=(120,25))
		jia=wx.Button(bgp,label='+',size=(60,25))
		jian=wx.Button(bgp,label='-',size=(60,25))
		cheng=wx.Button(bgp,label='*',size=(60,25))
		chu=wx.Button(bgp,label='/',size=(60,25))
		equal=wx.Button(bgp,label='=',size=(80,25))
		self.myRe=wx.TextCtrl(bgp,wx.TE_READONLY,size=(120,25))

		mBox=wx.BoxSizer(wx.VERTICAL)
		mBox.Add(jia,wx.ALL,border=5)
		mBox.Add(jian,wx.ALL,border=5)
		mBox.Add(cheng,wx.ALL,border=5)
		mBox.Add(chu,wx.ALL,border=5)

		box=wx.BoxSizer()
		box.Add(self.qian,1,wx.ALIGN_CENTER|wx.ALL,border=5)
		box.Add(mBox,0,wx.ALL,border=5)
		box.Add(self.hou,1,wx.ALIGN_CENTER|wx.ALL,border=5)
		box.Add(equal,0,wx.ALL|wx.ALIGN_CENTER,border=5)
		box.Add(self.myRe,1,wx.ALIGN_CENTER|wx.ALL,border=5)

		jia.Bind(wx.EVT_BUTTON,self.__Jia)
		jian.Bind(wx.EVT_BUTTON,self.__Jian)
		cheng.Bind(wx.EVT_BUTTON,self.__Cheng)
		chu.Bind(wx.EVT_BUTTON,self.__Chu)
		equal.Bind(wx.EVT_BUTTON,self.__Equal)

		bgp.SetSizer(box)

	def __Jia(self,evt):
		self.__fu='+'
	def __Jian(self,evt):
		self.__fu='-'
	def __Cheng(self,evt):
		self.__fu='*'
	def __Chu(self,evt):
		self.__fu='/'
	def __Equal(self,evt):
		self.__qian=self.qian.GetValue()
		self.__hou=self.hou.GetValue()
		if self.__fu == '+':
			self.__result=float(self.__qian) + float(self.__hou)
		elif self.__fu=='-':
			self.__result=float(self.__qian) - float(self.__hou)
		elif self.__fu=='*':
			self.__result=float(self.__qian) * float(self.__hou)
		elif self.__fu== '/':
			if self.__hou == '0':
				self.__result='ERROR'
			else:
				self.__result=float(self.__qian) / float(self.__hou)
		else:
			pass

		self.myRe.SetValue(str(self.__result))

c=Calculation()