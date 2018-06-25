if __name__=='__main__':
    import createDataSet
    import kNN
    (group,labels) = createDataSet.createDataSet()
    print(kNN.classify0([0.8,0.7],group,labels,3))
