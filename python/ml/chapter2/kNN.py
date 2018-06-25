'''
kNN: k近邻算法
输入:   inX: 待分类的向量 (1xN)
        dataSet: M个N维向量组成的矩阵 (M*N)
        labels:  数据集标签 (1xM)
        k: 要比较的邻居个数 (奇数)
            
输出:   inx要分入的类别
'''

from numpy import *
import operator #运算符模块,k邻近算法采用这个模块进行排序

#k-近邻算法
def classify0(inX,dataSet,labels,k): #inX:输入向量；dataSet:训练数据集；labels：标记；k：最近邻居数
    dataSetSize = dataSet.shape[0] #训练数据集行数，样本个数
    diffMat = tile(inX,(dataSetSize,1))-dataSet #先沿着第0维重复4次，再沿着第一维重复1次，变成和数据集一样的数组；
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1) #按行求和
    distances = sqDistances**0.5 #距离
    sortedDistIndicies = distances.argsort() #升序排序，返回索引
    classCount = {} # 创建字典，将用于存放key+value
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1 #返回字典中key对应的value值，否则返回0;这句执行的结果就是voteIlabel这个key对应类别的个数value
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #items返回列表，要从大到小排序，按照operate获取的第二维数据
    return sortedClassCount[0][0] #第一个0为次数最多的类别在列表第一个元素，第二个0是key+value中的key，代表类别