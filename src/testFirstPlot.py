from numpy import array
from numpy import *
import knn

import matplotlib.pyplot as plot

datingMat, datingLabels = knn.readDataFile("../inaction/Ch02/datingTestSet2.txt")

fig = plot.figure()
ax = fig.add_subplot(111)
datingMat2 = {}
handles = []
distinctLabels = []
size = len(datingLabels)
for index in range(size):
    label = datingLabels[index];    
    labelMatrix = datingMat2.get(label);
    if labelMatrix is None :
        labelMatrix = []
        datingMat2[label] = labelMatrix
    labelMatrix.append(datingMat[index, :])
a=mat(datingMat2.get(1))
b=mat(datingMat2.get(2))
c=mat(datingMat2.get(3))
print a[:,1][0]
print b[:,1][0]
print c[:,1][0]
handles.append(ax.scatter(a[:, 0], a[:, 1], tile(15,(a.shape[0])), tile(15,(a.shape[0]))))
handles.append(ax.scatter(b[:, 0], b[:, 1], tile(20,(b.shape[0])), tile(20,(b.shape[0]))))
handles.append(ax.scatter(c[:, 0], c[:, 1], tile(30,(c.shape[0])), tile(30,(c.shape[0]))))
#ax.axis([0, 100000, -2, 25])
#ax.axis([0, 100000, -2, 25])
#ax.axis([0, 100000, -2, 25])
plot.ylabel('Percentage of Time Spent Playing Video Games')
plot.xlabel('Liters of Ice Cream Consumed Per Week')
plot.legend(handles, ["I do not like it", "b", "c"])

plot.show()
