class hgf:
	name='hgf'
	age=21
	__var='class private attribute'

	def __getName(self):
		print self.name
		print 'private\n'

	def __getAge(self):
		print self.age
		print 'private\n'

	def getInfo(self):
		self.__getName()
		self.__getAge()
		print 'public\n'

	def otherSet(self):
		self.__var2='instance private attribute'
		print self.__var
		print self.__var2

	def dealPri(self,ss):
		self.__var2=ss
		print self.__var2
		print id(self)

	def p(self):
		print self.__var2

	@classmethod
	def classInfo(self):
		print 'class'
		print self.name
		print self.age

	@staticmethod
	def staticInfo():
		print hgf.name
		print hgf.age
		print 'static\n'

a,b=hgf(),hgf()
a.dealPri('aaaa')

b.dealPri('bbbb')
a.p()
b.p()