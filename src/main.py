import knn
groups,labels=knn.createDataSet()
mylabel=knn.classify0([0,0],groups,labels,3)
print "mylabel is :"+mylabel