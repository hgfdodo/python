class ren:
	name='human'
	age='unknow'

	def fun(self):
		print "ren:" +self.name

	def __init__(self):
		self.name='as'
		self.xxxx='xxxxx'

	def px(self):
		print self.xxxx

class an:
	name='animal'
	jiao='a~a~'

	def __init__(self):
		self.name='ddd'

	def fun(self):
		print self.jiao

class a(an,ren):
	
	def __init__(self):
		pass#ren.__init__(self)

x=a()
print "name:" + x.name
x.fun()
#x.px()