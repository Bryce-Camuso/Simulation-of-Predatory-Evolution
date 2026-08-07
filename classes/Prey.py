from .Animal import Animal
from .Plant import Plant
import random
from .StaticMap import StaticMap

global debug
debug = False

class Prey(Animal):
    
    
    def __init__(self, speed, stealth, stamina, sense, position):
        self._escaped = False
        super().__init__(speed, stealth, stamina, sense, position)

    # Helper Functions
    def _cellWeight(self, point, map):
        checkMap = map.get_map_point(point)
        if checkMap is None:
            return None
        if checkMap[1] == 1:
            return 1
        elif checkMap[1] == 3:
            return 1
        
    def _searching_tile_weight(self, tileNum):
        if tileNum == 1:
            return 15
        if tileNum == 2:
            return -100
        if tileNum == 3:
            return 15
        
    def _stalking_tile_weight(self, tileNum):
        if tileNum == 1:
            return 15
        if tileNum == 2:
            return -100
        if tileNum == 3:
            return 20
        
    def _pursuit_tile_weight(self, tileNum):
        if tileNum == 1:
            return 20
        if tileNum == 2:
            return -100
        if tileNum == 3:
            return 50
    
    
    

    
    def _searching_weight(self, tile, flowerScentLookup, targetPos, movementNoise, midpoint):
        global debug
        tilePos, tileType = tile
        tileWeight = self._searching_tile_weight(tileType)
        scentWeigthFlower = flowerScentLookup.get(tilePos,0)
        midpush = self._distance((midpoint,midpoint), tilePos) // 20 # this was added to help push both animals towards the middle of the map for more consistant interactions.
        #movementNoise = random.randint(-5,5)


        if debug:
            movementNoise = 0
        if tilePos == targetPos: target = 100
        else: target = 0
        return (tilePos,  (tileWeight + scentWeigthFlower + movementNoise + target - midpush))
    
    def _stalking_weight(self, tile, predatorScentLookup, flowerScentLookup, targetPos, movementNoise):
        global debug
        tilePos, tileType = tile
        tileWeight = self._stalking_tile_weight(tileType)
        scentWeigthFlower = flowerScentLookup.get(tilePos,0)
        scentWeigthPredator = predatorScentLookup.get(tilePos, 0) // 2
        #movementNoise = random.randint(-5,5)
        if debug:
            movementNoise = 0
        if tilePos == targetPos: target = 100
        else: target = 0
        return (tilePos,  (tileWeight + (scentWeigthFlower - scentWeigthPredator) + movementNoise + target))
    
    def _pursuit_weight(self, tile, predatorScentLookup):
        tilePos, tileType = tile
        tileWeight = self._pursuit_tile_weight(tileType)
        scentWeigthPredator = predatorScentLookup.get(tilePos, 0) * 2
        
        return (tilePos,  (tileWeight - scentWeigthPredator))
        
    def _get_max_weight(self, predator, flower, map, phase):
        searchArea = self.search(self.get_sense() // 2)
        mapSearchReturn = map.get_map_list(searchArea)
        flowerScentTrail = flower.get_scent().get_scent_trail(self.get_sense())
        flowerPosition = flower.get_position()
        predatorScentTrail = predator.get_scent().get_scent_trail(self.get_sense())

        randomList = random.choices(range(-5, 5), k=len(mapSearchReturn))

        maxWeight = ((-1,-1), -2000)
        if phase == 1:
            flowerScentLookup = self._scent_list_lookup_builder(flowerScentTrail)
            midpoint = map.get_map_limit() // 2
            for i in mapSearchReturn:
                returnValue = self._searching_weight(i, flowerScentLookup, flowerPosition, randomList[-1], midpoint)
                randomList.pop()
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 2:
            flowerScentLookup = self._scent_list_lookup_builder(flowerScentTrail)
            predatorScentLookup = self._scent_list_lookup_builder(predatorScentTrail)
            for i in mapSearchReturn:
                returnValue = self._stalking_weight(i, predatorScentLookup, flowerScentLookup, flowerPosition, randomList[-1])
                randomList.pop()
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 3:
            predatorScentLookup = self._scent_list_lookup_builder(predatorScentTrail)
            for i in mapSearchReturn:
                returnValue = self._pursuit_weight(i, predatorScentLookup)
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        return maxWeight
    

    #Methods

    def get_escaped(self):
        return self._escaped
    
    def set_escaped(self, newValue):
        if not isinstance(newValue, bool):
            raise TypeError('New Value must be a bool type')
        self._escaped = newValue
          
    def get_move_list(self, predator, flower, map, phase):
        '''
        phase is given as an int according to the table below

        searching phase = 1
        stalking phase = 2
        pursuit phase = 3
        '''
        if self.get_energy() >= 0:
            #potentily add a check for if how much enrgy is left to use and remove final points from list
            maxWeight = self._get_max_weight(predator, flower, map, phase)
            return self.pathfinding(maxWeight[0], map)
        else: return []
        
    def strugle(self, predator):
        energy = self.get_energy()
        predatorEnergy = predator.get_energy()

        if energy > predatorEnergy:
            randNum = random.randint(0, self._ENERGYTOTAL)
            if randNum <= energy:
                self.substract_energy(randNum)
                return True

        return False
    


def tester(): 
    global debug
    debug = True

    testPrey = Prey(40, 40, 40, 40, (25,25))
    testMap = StaticMap()
    testPredator = Animal(10, 10, 10,10, (15,10))
    testPlant = Plant((30,30))

    #getters 
    print('Getters')

    if testPrey.get_escaped() == False:
        print('escaped: pass')
    else:
        print('escaped: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters
    print('\nSetters')
    
    testPrey.set_escaped(True)
    if testPrey.get_escaped() == True:
        print('escaped: pass')
    else:
        print('escaped: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters errors
    print('\nSetters Errors')

    try:
        testPrey.set_escaped(0)
        print('Error: None')
    except TypeError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    print('---------------------------------------------------------------------------------------------------------------------')
    #test set 2) methods
    print('\nGet Move List')

    print('\nPhase 1 (searching) test')

    # stuck on how to test a function with randomness built in.

    testMoveList = testPrey.get_move_list(testPredator, testPlant, testMap, 1)
    exampleMoveList = [(25, 25), (25, 26), (25, 27), (25, 28), (25, 29), (26, 29), (27, 29), (28, 29), (29, 29), (29, 30), (30, 30)]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 2 (Stalking) test')
    testMoveList = testPrey.get_move_list(testPredator, testPlant, testMap, 2)
    exampleMoveList = [(25, 25), (25, 26), (25, 27), (25, 28), (25, 29), (26, 29), (27, 29), (28, 29), (29, 29), (29, 30), (30, 30)]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 3 (pursuit) test')
    testMoveList = testPrey.get_move_list(testPredator, testPlant, testMap, 3)
    exampleMoveList = [(25, 25), (25, 26)]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag and testMap.get_map_point((25,26))[1] == 3:
        print('Move List: pass')
    else:
        print('Move List: false')


    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nStrugle')
    testPrey._energyLeft = 10000

    testPredator.energy_used()

    if testPrey.strugle(testPredator) == True:
        print('strugle success: pass')
    else:
        print('strugle success: fail')
    
    energy = testPrey.get_energy()
    testPrey.substract_energy(energy - 1)

    if testPrey.strugle(testPredator) == False:
        print('strugle fail: pass')
    else:
        print('strugle fail: fail')

if __name__ == '__main__':
    tester()