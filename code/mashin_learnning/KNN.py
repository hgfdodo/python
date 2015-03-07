#coding:utf-8
from numpy import *
import operator
class KNN:
	def createDataSet(self):
		group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
		labels = ['A','A','B','B']
		return group,labels

	def file2Matrix(self,filePath):
		file_handle = open(filePath,'r')
		fileLines = file_handle.readlines()
		numberOfLine = len(fileLines)
		returnMat = zeros((numberOfLine,3))
		classLabelVector=[]
		index = 0

		for line in fileLines:
			line = line.strip()
			listFormLine = line.split("\t")
			returnMat[index,:] = listFormLine[0:3]
			classLabelVector.append(listFormLine[-1])
			index+=1
		return returnMat,classLabelVector


	def classify0(self,intX,dataSet,labels,k):
		"""
		function：	knn邻近算法【分类】:选取与intX距离最近的K个点的类别中，最集中的类别为intX的类别

		intX:		待分类的输入向量
		dataSet：	数据矩阵
		labels:		数据矩阵每一行对应的类别标号
		k:			总共的类别数

		return：		intX向量被分类的类别标号
		"""
		dataSetSize = dataSet.shape[0]
		diffMat = tile(intX,(dataSetSize,1))-dataSet
		sqDiffMat = diffMat**2
		sqDistance = sqDiffMat.sum(axis=1)
		distance = sqDistance**0.5
		sortDisIndex = distance.argsort()

		classCount={}

		for x in range(k):
			voteLabel = labels[sortDisIndex[x]]
			classCount[voteLabel] = classCount.get(voteLabel,0) + 1
		sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

		return sortedClassCount[0][0]
		

	def autoNorm(self,dataSet):
		"""
		归一化处理：（value-min）/（max-min）

		"""
		dataMin = dataSet.min(0)		#每一列的最小值
		dataMax = dataSet.max(0)		#每一列的最大值
		normDataSet = zeros(shape(dataSet))
		ranges = dataMax - dataMin
		#上句和这句一样：ranges = dataSet.ptp(0)
		m = dataSet.shape[0]
		normDataSet = dataSet-tile(dataMin,(m,1))
		normDataSet = normDataSet/tile(ranges,(m,1))

		return normDataSet,ranges,dataMin

	def classTestValidate(self, testPercent, filePath):
		"""
		自动将文档中的数据读入内存，最后一列为类标号
		自动分配测试数据和训练数据
		得出正确率和错误率，评价
		"""
		dataMat,labels = self.file2Matrix(filePath)
		dataSize = dataMat.shape[0]
		testSize = int(dataSize*testPercent)
		normDataSet,ranges,datamin = self.autoNorm(dataMat)
		classifyResult=[]
		errorCount=0.0
		for i in range(testSize):
			classLabel = self.classify0(normDataSet[i,:], normDataSet[i:dataSize,:], labels[i:dataSize], 3)
			print classLabel
			classifyResult.append( classLabel )
			if(classLabel != labels[i]):
				errorCount += 1
		print "error percent :"
		print (errorCount/float(testSize))

"""
filePath1 = r"test.txt"
filePath2 = r"datingTestSet2.txt"
k = KNN()
mat,labels = k.file2Matrix(filePath2)
matTest,labelTest = k.file2Matrix(filePath1)
normDataSet,ranges,dataMin=k.autoNorm(mat)

size = matTest.shape[0]
normTest = ( matTest-tile(dataMin,(size,1)) ) / ( tile(ranges,(size,1)) )
print size
print normTest
classI=[]
for i in range(size):
	classI.append( k.classify0(normTest[i],normDataSet,labels,3) )
print classI
print labelTest
"""
k = KNN()
k.classTestValidate(0.1,r"datingTestSet2.txt")