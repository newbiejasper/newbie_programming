'''
测试kNN分类算法的分类效果
输入:   filename:原始数据文件名
        m:特征数
        hoRatio:数据集中百分之多少用来作Test
输出：分类错误率
'''
import txtfile2matrix
import normalization
import kNN

def datingClassTest(filename,m,hoRatio):
    datingDataMat,classLabelVector = txtfile2matrix.file2matrix(filename,m)
    datingLabels = txtfile2matrix.char2int(classLabelVector)
    normMat,ranges,minVals = normalization.autoNorm(datingDataMat)
    m = normMat.shape[0] #样本个数
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNN.classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with:%d,the real answer is:%d" %(classifierResult,datingLabels[i]))
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("the total error rate is:%f" %(errorCount/float(numTestVecs)))
