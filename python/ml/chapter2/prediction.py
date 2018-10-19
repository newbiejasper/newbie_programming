'''
prediction:预测类别
输入： 
'''

import numpy as np
import txtfile2matrix
import normalization
import kNN

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,classLabelVector = txtfile2matrix.file2matrix("C:/Users/jasper/iCloudDrive/newbie_programming/python/ml/chapter2/datingTestSet.txt",3)
    datingLabels = txtfile2matrix.char2int(classLabelVector)
    normMat, ranges, minVals = normalization.autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream,],dtype=float)
    classifierResult = kNN.classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print("You will probably like this person: %s" % (resultList[classifierResult - 1]))

