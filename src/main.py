import knn

import matplotlib.pyplot as plot
groups,labels=knn.createDataSet()
mylabel=knn.classify0([0,0],groups,labels,3)
print "mylabel is :"+mylabel
datingMat,datingLabels=knn.readDataFile("../inaction/Ch02/datingTestSet.txt")
fig=plot.figure()
ax=fig.add_subplot(111)
ax.scater(datingMat[:,1],datingLabels[:,2])
plot.show()