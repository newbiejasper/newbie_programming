from numpy import array
#创建模拟数据集
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]) #一行就是一个样本，有4个样本
    labels = ['A','A','B','B'] #对应每个样本的标签，4个标签
    return group,labels