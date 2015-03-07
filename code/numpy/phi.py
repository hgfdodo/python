import numpy
def phi(aago,ago):
	return aago+ago
def main():
	zero=0
	one=1
	cur=0
	re=[]
	while cur < 4000000:
		cur=phi(zero,one)
		re.append(cur)
		zero=one
		one=cur
	ree=numpy.array(re)
	result=ree[ree%2==0]
	print result

if __name__=="__main__":
	main()