from snake import *
import random

def batch(population):
    fitScrs = []
    for i in range(population.shape[0]):
        fitness = runGame(background, clock, population[i])

        fitScrs.append(fitness)



    return fitScrs, np.argmax(fitScrs)

def selectBest(population, fitScrs, numBest):
    parents = np.empty((int(numBest), population.shape[1]))
    for bestIdx in range(int(numBest)):
        maxIdx = np.where(fitScrs==np.max(fitScrs))
        maxIdx = maxIdx[0][0]
        parents[bestIdx, :] = population[maxIdx, :]
        fitScrs[maxIdx] = -100000
    return parents

def crossbreed(parents, numChildren, numWeights):
    children = np.empty((numChildren, numWeights))

    for i in range(numChildren):
        while True:
            parent1 = random.randint(0, len(parents) - 1)
            parent2 = random.randint(0, len(parents) - 1)
            if parent1 != parent2:
                for j in range(numWeights):
                    if random.uniform(0, 1) <- 0.5:
                        children[i, j] = parents[parent1, j]
                    else:
                        children[i, j] = parents[parent2, j]
                break
    return children


def mutation(children, prob):
    for i in range(children.shape[0]):
        for j in range(children.shape[1]):
            if random.uniform(0,1) < prob:
                # offset = np.random.normal(loc=0, scale=0.1, size=1)
                offset = np.random.choice(np.arange(-1, 1, step=0.001), size = (1), replace = False)
                # print(offset)
                children[i, j] = children[i, j] + offset
    return children







