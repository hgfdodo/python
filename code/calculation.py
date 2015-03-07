#coding:utf-8
import wx
import math

class Calculation(wx.Frame):
	buttons=[]
	command=[]
	qian=0
	hou=0
	first=True
	fu=''



	def __init__(self):
		self.app=wx.App()
		wx.Frame.__init__(self,None,title="Simple Calculation",size=(500,300))
		self.Center()
		self.__showWin()
		self.Show()
		self.app.MainLoop()

	def __showWin(self):
		bgp=wx.Panel(self)

		self.result=wx.TextCtrl(bgp,style=wx.TE_MULTILINE|wx.TE_READONLY|wx.ALIGN_RIGHT)

		layout=wx.GridSizer(4,5,4,4)
		t=[]
		fu=['','+','-','*','/']
		handleNum=[
		self.__On0,
		self.__On1,
		self.__On2,
		self.__On3,
		self.__On4,
		self.__On5,
		self.__On6,
		self.__On7,
		self.__On8,
		self.__On9]

		handleFu=['',
		self.__OnJia,
		self.__OnJian,
		self.__OnCheng,
		self.__OnChu]

		for i in range(1,10):
			tmpBt = wx.Button(bgp,label=str(i))
			t.append(tmpBt)

			tmpBt.Bind(wx.EVT_BUTTON,handleNum[i])
			if(i%3==0):
				t.append(wx.StaticText(bgp))
				tmpBt2 = wx.Button(bgp,label=fu[i/3])
				t.append(tmpBt2)
				tmpBt2.Bind(wx.EVT_BUTTON,handleFu[i/3])

		bt0=wx.Button(bgp,label='0')
		t.append(bt0)
		bt0.Bind(wx.EVT_BUTTON,handleNum[0])

		btE=wx.Button(bgp,label='=')
		t.append(btE)
		btE.Bind(wx.EVT_BUTTON,self.onEqual)

		t.append(wx.StaticText(bgp))
		t.append(wx.StaticText(bgp))

		btDiv=wx.Button(bgp,label='/')
		t.append(btDiv)
		btDiv.Bind(wx.EVT_BUTTON,handleFu[4])

		self.buttons=t


		layout.AddMany(t)

		calPanel=wx.BoxSizer(wx.VERTICAL)
		calPanel.Add(self.result,1,wx.EXPAND|wx.ALL,border=5)
		calPanel.Add(layout,1,wx.EXPAND|wx.ALL,border=5)

		bgp.SetSizer(calPanel)

	def onEqual(self,evt):
		finalResult = 0

		if self.first:
			self.qian = self.__dealNum()
			self.first=False
			self.command=[]
		else:
			self.hou = self.__dealNum()
			self.command=[]

		if self.fu=='+':
			finalResult = self.qian+self.hou
		elif self.fu=='-':
			finalResult = self.qian-self.hou
		elif self.fu=='*':
			finalResult = self.qian*self.hou
		elif self.fu=='/':
			if self.hou==0:
				self.result.AppendText('\n' + 'Error\n')
			else:
				finalResult = self.qian/self.hou
		else:
			self.result.AppendText('\n' + str(self.qian) + '\n')


		self.result.AppendText('\n' + str(finalResult) + '\n')


		self.command=[]
		self.first=True
		self.qian=0
		self.hou=0

	def __dealNum(self):
		length=len(self.command)
		x=0
		result = 0
		for i in self.command:
			result += i*math.pow(10,length-x-1)
			x += 1
		return result


	def __On0(self,evt):
		self.command.append(0)
		str1=self.result.AppendText('0')
	def __On1(self,evt):
		self.command.append(1)
		str1=self.result.AppendText('1')
	def __On2(self,evt):
		self.command.append(2)
		str1=self.result.AppendText('2')
	def __On3(self,evt):
		self.command.append(3)
		str1=self.result.AppendText('3')
	def __On4(self,evt):
		self.command.append(4)
		str1=self.result.AppendText('4')
	def __On5(self,evt):
		self.command.append(5)
		str1=self.result.AppendText('5')
	def __On6(self,evt):
		self.command.append(6)
		str1=self.result.AppendText('6')
	def __On7(self,evt):
		self.command.append(7)
		str1=self.result.AppendText('7')
	def __On8(self,evt):
		self.command.append(8)
		str1=self.result.AppendText('8')
	def __On9(self,evt):
		self.command.append(9)
		str1=self.result.AppendText('9')

	def __OnJia(self,evt):
		str1=self.result.AppendText('+')

		self.qian += self.hou
		if self.first:
			self.qian = self.__dealNum()
			self.first=False
			self.command=[]
		else:
			self.hou = self.__dealNum()
			self.command=[]
		self.fu='+'
		

	def __OnJian(self,evt):
		str1=self.result.AppendText('-')

		self.qian -= self.hou
		if self.first:
			self.qian = self.__dealNum()
			self.first=False
			self.command=[]
		else:
			self.hou = self.__dealNum()
			self.command=[]
		self.fu='-'
		
	def __OnCheng(self,evt):
		str1=self.result.AppendText('*')
		self.qian *= self.hou
		if self.first:
			self.qian = self.__dealNum()
			self.first=False
			self.command=[]
		else:
			self.hou = self.__dealNum()
			self.command=[]
		self.fu='*'

	def __OnChu(self,evt):
		str1=self.result.AppendText('/')
		if not self.hou == 0:
			self.qian = self.qian / self.hou
		if self.first:
			self.qian = self.__dealNum()
			self.first=False
			self.command=[]
		else:
			self.hou = self.__dealNum()
			self.command=[]
		self.fu='/'

c = Calculation()
