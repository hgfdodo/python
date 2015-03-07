
# -*- coding: utf-8 -*-

import wx

"""
将窗体居中显示
"""

class MyFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,None)
        #居中
        self.Center()
        #显示
        self.Show()

if __name__=='__main__':
    #初始化程序
    app=wx.App()
    #创建窗体
    MyFrame()
    #开始消息循环
    app.MainLoop()