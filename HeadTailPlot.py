import random, pylab
def flipPlot(minExp,maxExp):
    "minExp and maxExp is positive integers, and minExp<maxExp to plot 2**minExp to 2**maxExp times flips results."
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random()<0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title("Difference Between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads - #Tails)")
    pylab.plot(xAxis,diffs,'bo')
    pylab.semilogx()
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel("#Heads/#Tails")
    pylab.plot(xAxis,ratios,'bo')
    pylab.semilogx()
    pylab.show()
    
random.seed(0)
flipPlot(4,20)
