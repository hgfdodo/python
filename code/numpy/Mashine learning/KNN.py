import numpy
import operator
import matplotlib.pyplot

def createDataSet():
	group=numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=numpy.array(['A','A','B','B'])
	return group,labels

def classify(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diff = numpy.tile(inX,(dataSetSize,1)) - dataSet
	sqDiff = diff**2
	tmp = sqDiff.sum(axis=1)
	distance = tmp**0.5
	sortedIndices = distance.argsort()
	classCount={}
	for  i in range(k):
		votelabel = labels[sortedIndices[i]]
		classCount[votelabel] = classCount.get(votelabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

#filename: the file where it stored
#n:a vector has n properties, (classify line is not in n)
def file2matrix(filename,n):
	f=open(filename)
	lines = f.readlines()
	dataSize=len(lines)
	returnMatrix = numpy.zeros((dataSize,n))
	classifyLabels=[]
	index = 0
	for line in lines:
		vector=line.strip()
		lineValues=vector.split("\t")
		returnMatrix[index,:] = lineValues[0:n]
		classifyLabels.append(lineValues[-1])
		index +=1
	return returnMatrix,classifyLabels
def show(matrix):
	fig=matplotlib.pyplot.figure()
	ax=fig.add_subplot(111)
	ax.scatter(matrix[:,1],matrix[:,2])
	matplotlib.pyplot.show()

if __name__ == "__main__":
	#43757	7.882601	1.332446	largeDoses
	dataSet,labels=file2matrix(r"E:\python\code\numpy\Mashine learning\datingTestSet.txt",3)
	show(dataSet)
	inX=[43757,7.882601,1.332446]
	print classify(inX,dataSet,labels,90)