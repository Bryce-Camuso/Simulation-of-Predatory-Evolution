import sys
import random
sys.path.append('classes/')
from classes.Animal import Animal
from classes.Map import Map

testMap = Map()

testPredator = Animal(60, 20, 40, 100, (50,50))
testPrey = Animal(40, 30, 40, 50, (30, 30))
testPlant = Animal(40, 30, 40, 50, (10, 10)) # this makes no sence but is the only way I can think to make it work without a full implemtation at the moment.

# these functions will be put in the Predator and prey classes
def tileToWeight(tileNum):
    if tileNum == 1:
        return 15
    if tileNum == 2:
        return -100
    if tileNum == 3:
        return 20

def searchScent(scentList, position):
    scentStrength = 100
    scentList.reverse()
    for i in scentList:
        if position in i:
            return scentStrength
        else:
            scentStrength -= 5
    return 0



def weightFunction(tile, scentList, targetPos):
    tileWeight = tileToWeight(tile[1])
    scentWeigth = searchScent(scentList, tile[0]) // 2
    movementNoise = random.randint(-5,5)
    if tile[0] == targetPos: target = 100
    else: target = 0
    return (tile[0],  (tileWeight + scentWeigth + movementNoise + target))

def get_max_weight(animal, target, map):
    searchArea = animal.search(50)
    mapSearchReturn = map.get_map_list(searchArea)
    targetScentTrail = target.get_scent().get_scent_trail(animal.get_sense())

    maxWeight = ((-1,-1), -2000)
    for i in mapSearchReturn:
        returnValue = weightFunction(i, targetScentTrail, target.get_position())
        if returnValue[1] > maxWeight[1]:
            maxWeight = returnValue
    return maxWeight


testPlant.update_scent_trail()
testPrey.update_scent_trail()

while True:
    maxWeight = get_max_weight(testPrey, testPlant, testMap)
    preyMovement = testPrey.pathfinding(maxWeight[0], testMap)[-1]
    testPrey.set_position(preyMovement[1])
    testPrey.scent_decay()
    testPrey.update_scent_trail()
    print('prey move: ' + str(testPrey.get_position()))


    maxWeight = get_max_weight(testPredator, testPrey, testMap)
    predMovement = testPredator.pathfinding(maxWeight[0], testMap)[-1]
    testPredator.set_position(predMovement[1])
    print('pred move: ' + str(testPredator.get_position()))
    if testPrey.get_position() == testPredator.get_position():
        print('Predator caught prey')
        break
    