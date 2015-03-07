#coding:utf-8
import time
import threading

class MyThread(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self,name=threadName)

	def run(self):
		global x
		lock.acquire()
		print self.name,x
		x=x+1
		time.sleep(1)
		lock.release()

lock=threading.RLock()

t=[]
for i in range(5):
	th=MyThread(str(i))
	print th
	t.append(th)
x=0

for i in t:
	i.start()


