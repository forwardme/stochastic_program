def stdDev(X):
    """假设X是一个数字列表
       返回X的标准差"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5