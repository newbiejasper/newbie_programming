import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import txtfile2matrix

datingDataMat,classLabelVector = txtfile2matrix.file2matrix("C:/Users/jasper/iCloudDrive/newbie_programming/python/ml/chapter2/datingTestSet.txt",3)
datingLabels = txtfile2matrix.char2int(classLabelVector)

fig = plt.figure() #创建一个新图形
ax = fig.add_subplot(111) #例如349，则把画布分成3行4列，在第9块画图
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
plt.show()