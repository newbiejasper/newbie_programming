'''
normalization:数值归一化
输入：dataSet
输出：normDataSet(归一化之后的数据)
'''

import numpy as np

def autoNorm(dataSet):
    minVals = dataSet.min(0) #列的最小值
    maxVals = dataSet.max(0) #列的最大值
    ranges = maxVals-minVals
    normDataSet = np.zeros(np.shape(dataSet)) #创建和原数据集尺寸相当的数组
    m = dataSet.shape[0] #dataSet的行数
    normDataSet = dataSet-np.tile(minVals,(m,1)) #把最小值的数组沿着行方向重复m次，列方向一次
    normDataSet = normDataSet/np.tile(ranges,(m,1)) 
    return(normDataSet,minVals)