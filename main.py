from ga import *
from snake import *
from datetime import datetime

popSize = 50
# numGens = 500
crossbreedProb = 0.2
mutationProb = 0.1

numWeights = 243

pop = (popSize, numWeights)
population = np.random.choice(np.arange(-1, 1, step = 0.01), size = pop, replace = True)

instance = str(time.time())

output = 'output.' + instance + '.txt'

#saves the weights of the best snakes from each generation
snakes = 'output.' + instance + '.txt'

bestSnakes = []
gen = 0
# for gen in range(numGens):
while True:


    fitScrs, bestIdx = batch(population)
    best = np.max(fitScrs)
    print(best)
    bestSnakes.append(best)

    o = open(output,"a+")
    o.write("Generation: " + str(gen) + '\n')
    o.write("Best Fitness: " + str(best) + '\n')
    last20 = bestSnakes[len(bestSnakes) - 20:]
    avg = sum(last20) / 20
    o.write("Running avg: " + str(avg) + '\n')
    o.close()

    s = open(snakes, "a+")
    s.write("Generation: " + str(gen) + ' Fitness: ' + str(best) + ' Weights: ' + '\n')
    bestWeights = population[bestIdx]
    bw = ''
    for x in bestWeights:
        bw += str(x) + ', '
    s.write(bw + '\n')
    s.close()
    

    parents = selectBest(population, fitScrs, int(crossbreedProb * popSize))

    children = crossbreed(parents, popSize - parents.shape[0], numWeights)

    children = mutation(children, mutationProb)

    gen += 1

    