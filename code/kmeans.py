#coding:utf8
import random
import math
import copy

dim=5
k=4
dataset=150

#读取文件
def readfile(filepath):
	l=[]
	p=[]
	i=1
	f=open(filepath,'r')
	for line in f:
		tmp=line.strip('\n').split(',')
		p=map(float,tmp)
		p.insert(0,str(i))
		i+=1
		l.append(p)
	return l

#获取两元祖（点）的欧氏距离（每个元组的第一个元素是数据序号）
def getDist(tuple1,tuple2):
	sum=0
	for i in range(1,len(tuple1)):
		sum+=(tuple1[i]-tuple2[i])*(tuple1[i]-tuple2[i])
	return math.sqrt(sum)

#比较一个元组数据与k个质心的距离，将该点分配到距离最短的集合中
def classify(means,mtuple):
#	print "means:",means
#	print "mtuple:",mtuple
	dis=getDist(means[0],mtuple)
#	print "dis:",dis
	label=0
	for i in range(1,k):
		tmp=getDist(means[i],mtuple)
		if(tmp < dis):
			dis=tmp
			label=i
#		print "dis2:",tmp,"# label2",label
	
	return label

#求误差：中心质点与该集合的各点的欧氏距离的和
def wucha(means,cluster):
	var=0
	for i in range(k):
		for j in range(len(cluster[i])):
			var += getDist(means[i],cluster[i][j])
	return var

#求当前集合的各个维度的平均值
def getmeansavg(jihei):
	t=[]
	for i in range(dim):
		t.append(0)

	for yuanzu in jihei:
		for weidu in range(1,dim+1):
			t[weidu-1]+=yuanzu[weidu]

	for i in range(dim):
		if len(jihei):
			t[i]=t[i]/len(jihei)
		else:
			t[i]=0

	return t
#找出与mtuple最近的means分量
def findmeans(junzhimean,jihei):
	dis=getDist(junzhimean,jihei[0])
	ret=jihei[0]
	for yuanzu in jihei[1:]:
		tmp=getDist(junzhimean,yuanzu)
		if(tmp < dis):
			ret=yuanzu

	return ret


#跟新means：以据类中每维数据的平均值作为新的means
def updatemeas(cluster):
	means=[]
	for jihe in cluster:
		tmp=getmeansavg(jihe)
		tmp.insert(0,'0')
		means.append(findmeans(tmp,jihe))
	return means

def printjihe(cluster):
	for jihe in cluster:
		print "######################################################111"
		for yuanzu in jihe:
			print yuanzu




#kmeans算法
def kmeans(tuples):
	i=0
	#质心点
	means=[]
	#分类集合
	cluster=[]
	#get random init means
	for x in range(k):
		means.append([])
	for x in range(k):
		cluster.append([])
	while i < k:
		ran=random.choice(range(1,dataset+1))
		if(len(means[ran%k])==0):
			print "ran",ran
			means[ran%k]=tuples[ran%dataset]
			
			i+=1
	#迭代
	for yuanzu in tuples:
		label=classify(means,yuanzu)
		cluster[label].append(yuanzu)

	new_var=wucha(means,cluster)
	old_var=-1
	while(abs(new_var - old_var) >=1):
		print means
		means=updatemeas(cluster)
		print "update means:",means

		old_var=new_var
		new_var=wucha(means,cluster)

		del cluster[:]
		for x in range(k):
			cluster.append([])

		for yuanzu in tuples:
			label=classify(means,yuanzu)
			#print "!!!!!!!!!label:", label
			cluster[label].append(yuanzu)
			#print "!!!!!!!!!!yuanzu:",yuanzu

	printjihe(cluster)


if __name__=="__main__":
	kmeans( readfile(r"e:\\testclass.txt"))