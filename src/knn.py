from numpy import tile
from numpy import array
from numpy import zeros
import operator
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(x,dataset,labels,k):
    print dataset
    size=dataset.shape[0]
    print size
    deltaMat=tile(x,(size,1))-dataset
    squreDeltaMat=deltaMat**2
    distances=squreDeltaMat.sum(axis=1)
    distances=distances**0.5
    sortedDistanceIndicies=distances.argsort()
    print sortedDistanceIndicies
    classCount={}
    for i in range(k):
        votelabel=labels[sortedDistanceIndicies[i]]
        classCount[votelabel]=classCount.get(votelabel,0)+1;
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0];

def readDataFile(filename):
    fr=open(filename)
    lines=fr.readlines();
    numberOfLines=len(lines);
    retMat=zeros((numberOfLines,3));
    labels=[]
    index=0
    for line in lines:
        line=line.strip();
        fields=line.split('\t');
        retMat[index,:]=fields[0:3]
        labels.append(int(fields[-1]))
        index+=1
    return retMat,labels