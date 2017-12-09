import random
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.05
            heads += 1
    return float(heads)/numFlips
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = float(sum(fracHeads))/len(fracHeads)
    return mean
print 'Heads ratio is : ',flipSim(100,100)
