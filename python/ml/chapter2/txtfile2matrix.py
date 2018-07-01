'''
file2matrix:将txt文件，以dataframe样子出现的的数据转化为矩阵和标签向量
输入：filename文件名,m是特征数
输出：returnMat训练样本矩阵，classLabelVector类标签向量

'''
import numpy as np

def file2matrix(filename,m):
    fr = open(filename)
    arrayOLines = fr.readlines() #逐行读取，以列表的形式返回
    numberOfLines = len(arrayOLines) #文件行数
    returnMat = np.zeros((numberOfLines,m)) #用于存放样本数据的矩阵
    classLabelVector = [] #用于存放标签向量
    index = 0
    for line in arrayOLines:
        line = line.strip() #截取掉所有的回车字符
        listFromLine = line.split('\t') #按照'\t'分割，返回列表，但是都是字符串
        returnMat[index,:] = listFromLine[0:m] #取前三列
        classLabelVector.append(listFromLine[-1]) #-1表示每行最后一个数，是标签数据
        index += 1
    return(returnMat,classLabelVector)

###把classLabelVector的字符串标签改为数字
def char2int(classLabelVector):
    for i in range(len(classLabelVector)):
        if classLabelVector[i] == "largeDoses":
            classLabelVector[i] = 3
        else:
            if classLabelVector[i] == "smallDoses":
                classLabelVector[i] = 2
            else:
                classLabelVector[i] = 1
    return(classLabelVector)
        

