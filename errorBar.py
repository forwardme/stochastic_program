import random, pylab
from stdDeviation import stdDev
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random()<0.5:
            heads += 1
    return heads/numFlips
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = float(sum(fracHeads))/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)

def showErrorBars( minExp, maxExp, numTrials):
    means, sds = [], []
    xVals = []
    for  exp in range( minExp,  maxExp+1):
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
        
    pylab.errorbar(xVals, means, yerr = 2*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads(' + str(numTrials) + 'trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')

showErrorBars(3,10,100)
pylab.show()
        