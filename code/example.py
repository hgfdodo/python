# -*- coding:utf-8 -*-
import threading
import time
class mythread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x                #设置全局变量
		lock.acquire()          #调用lock的acquire方法
		for i in range(3):
			x = x + 1
		time.sleep(1)
		print x
		lock.release()          #调用lock的release方法
lock = threading.RLock()        #生成Rlock对象
t1 = []
for i in range(10):
	t = mythread(str(i))
	print t
	t1.append(t)
x = 0                   #将全局变量的值设为0
for i in t1: 
	i.start()

