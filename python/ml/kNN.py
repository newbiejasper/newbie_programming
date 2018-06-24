from numpy import *
import operator #运算符模块,k邻近算法采用这个模块进行排序

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels