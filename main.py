from ga import *
from snake import *

popSize = 50
numGens = 500
crossbreedProb = 0.2
mutationProb = 0.1

numWeights = 243

pop = (popSize, numWeights)
population = np.random.choice(np.arange(-1, 1, step = 0.01), size = pop, replace = True)


bestSnakes = []

for gen in range(numGens):
    fitScrs = batch(population)
    best = np.max(fitScrs)
    print(best)
    bestSnakes.append(best)

    parents = selectBest(population, fitScrs, int(crossbreedProb * popSize))

    children = crossbreed(parents, popSize - parents.shape[0], numWeights)

    children = mutation(children, mutationProb)

    