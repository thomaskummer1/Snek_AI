import random, time, math
import numpy as np
import pygame

def init():
    headPos = [20, 20]
    snakeBody = [[20, 20], [21, 20]]
    foodPos = [random.randInt(0, 40), random.randInt(0, 40)]
    score = 0

    return headPos, snakeBody, foodPos, score

def play(headPos, snakeBody, foodPos, direction, score, background, clock):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        background.fill("#012a49")

        display(background, foodPos, snakeBody)
        snakeBody, foodPos, score = update(headPos, snakeBody, foodPos, direction, score)

        clock.tick(100000)

        return snakeBody, foodPos, score

def update(headPos, snakeBody, foodPos, direction, score):
    if direction == 'left':
        headPos[0] -= 1
    elif direction == 'right':
        headPos[0] += 1
    elif direction == 'up':
        headPos[1] -= 1
    else:
        headPos[1] += 1

    if headPos == foodPos:
        score += 1
        foodPos = [random.randInt(0, 40), random.randInt(0, 40)]
        while foodPos not in snakeBody:
            foodPos = [random.randInt(0, 40), random.randInt(0, 40)]
        snakeBody.insert(0, headPos)

    else:
        snakeBody.insert(0, headPos)
        snakeBody.pop()

    return snakeBody, foodPos, score 
    
        



def display(background, foodPos, snakeBody):
    for cell in snakeBody:
        cellrect = pygame.Rect(cell[0] * 10, cell[1] * 10, 10, 10)
        pygame.draw.rect(background, '#1s41j0', cellrect)
    foodrect = pygame.Rect(foodPos[0] * 10, foodPos[1] * 10, 10, 10)
    pygame.draw.rect(background, '4a920a', foodrect)



def runGame(background, clock, nnWeights):
    maxSteps = 3000
    stepsScore = 0

    headPos, snakeBody, foodPos, score = init()

    prevDir = ''
    ctSameDir = 0

    for i in range(maxSteps):
        # getting inputs for our NN

        # checking if cells around are blocked
        currDir = snakeBody[0] - snakeBody[1]
        leftDir = [currDir[1], -currDir[0]]
        rightDir = [-currDir[1], currDir[0]]

        forwardBlocked = isBlocked(snakeBody, currDir)
        leftBlocked = isBlocked(snakeBody, leftDir)
        rightBlocked = isBlocked(snakeBody,rightDir)

        foodDir = foodPos - snakeBody[0]

        # our direction and direction to food
        foodDirNorm = foodDir / np.linalg.norm(foodDir) 
        snakeDirNorm = currDir / np.linalg.norm(currDir)

        move = np.argmax(np.array(nn(np.array([
            foodDirNorm[0], foodDirNorm[1], snakeDirNorm[0], snakeDirNorm[1], forwardBlocked, leftBlocked, rightBlocked
        ]), nnWeights)))

        if move == prevDir: ctSameDir += 1
        else:
            ctSameDir = 0
            prevDir = move

        newDir = currDir
        if move == 'left':
            newDir = leftDir
        elif move == 'right':
            newDir = rightDir

        newHead = snakeBody[0] + newDir

        if newHead[0] < 0 or newHead[0] > 39 or newHead[1] < 0 or newHead[1] > 39:
            stepsScore -= 175
            break
        temp = False
        for i in snakeBody:
            if i == newHead:
                stepScore -= 175
                temp = True
        if temp:
            break

        snakeBody, foodPos, score = play(newHead, snakeBody, foodPos, move, score, background, clock)

        if ctSameDir > 10 and move == 'forward':
            stepsScore -= 1
        else:
            stepsScore += 2
    return score * 6000 + stepsScore

                
        





def isBlocked(snakeBody, currDir):
    newPos = snakeBody[0] + currDir
    
    if newPos[0] < 0 or newPos[0] > 39 or newPos[1] < 0 or newPos[1] > 39:
        return True
    
    for i in snakeBody:
        if i[0] == newPos[0] and i[1] == newPos[1]:
            return True
    return False
