import numpy as np

inputNodes = 7
hidden1 = 9
hidden2 = 15
outputNodes = 3

layer1IO = (hidden1, inputNodes)
layer2IO = (hidden2, hidden1)
layer3IO = (outputNodes, hidden2)

def getWeights(weights):
    l1cutoff = layer1IO[0] * layer1IO[1]
    l2cutoff = layer2IO[0] * layer2IO[1] + l1cutoff
    
    layer1W = weights[0:l1cutoff]
    layer2W = weights[l1cutoff:l2cutoff]
    layer3W = weights[l2cutoff:]

    return layer1W.reshape(layer1IO[0], layer1IO[1]), layer2W.reshape(layer2IO[0], layer2IO[1]), layer3W.reshape(layer3IO[0], layer3IO[1])

def predict(data, weights):
    weightsL1, weightsL2, weightsL3 = getWeights(weights)
    outL1 = np.matmul(weightsL1, data.T) # transpose for multiplication
    normL1 = np.tanh(outL1) # activation
    outL2 = np.matmul(weightsL2, normL1)
    normL2 = np.tanh(outL2)
    outL3 = np.matmul(weightsL3, normL2)
    dir = pickDir(outL3)
    return dir

def pickDir(weights):
    maxWeight = max(weights)
    idx = list(weights).index(maxWeight)
    if idx == 0:
        return 'left'
    elif idx == 1:
        return 'right'
    else:
        return 'forward'
            



