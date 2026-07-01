from Animal import Animal
from Map import Map
import random

class Prey(Animal):
    
    
    def __init__(self, speed, stealth, stamina, sense, position):
        self._escaped = False
        super().__init__(speed, stealth, stamina, sense, position)

    # Helper Functions
    def _cellWeight(self, point, map):
        checkMap = map.get_map_point(point)
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
    
    def _search_flower_scent(self, scentList, position):
        scentStrength = 100
        scentList.reverse()
        for i in scentList:
            if position in i:
                return scentStrength
            else:
                scentStrength -= 5
        return 0
    
    def _search_predator_scent(self, scentList, position):
        scentStrength = 100
        scentList.reverse()
        for i in scentList:
            if position in i:
                return scentStrength
            else:
                scentStrength -= 5
        return 0
    
    def _searching_weight(self, tile, predatorScentList, flowerScentList, targetPos):
        tileWeight = self._searching_tile_weight(tile[1])
        scentWeigthFlower = self._search_flower_scent(flowerScentList, tile[0])
        scentWeigthPredator = self._search_predator_scent(predatorScentList, tile[0]) //2
        movementNoise = random.randint(-5,5)
        if tile[0] == targetPos: target = 100
        else: target = 0
        return (tile[0],  (tileWeight + (scentWeigthFlower - scentWeigthPredator) + movementNoise + target))
    
    def _stalking_weight(self, tile, predatorScentList, flowerScentList, targetPos):
        tileWeight = self._stalking_tile_weight(tile[1])
        scentWeigthFlower = self._search_flower_scent(flowerScentList, tile[0]) // 2
        scentWeigthPredator = self._search_predator_scent(predatorScentList, tile[0])
        movementNoise = random.randint(-5,5)
        if tile[0] == targetPos: target = 100
        else: target = 0
        return (tile[0],  (tileWeight + (scentWeigthFlower - scentWeigthPredator) + movementNoise + target))
    
    def _pursuit_weight(self, tile, predatorScentList):
        tileWeight = self._pursuit_tile_weight(tile[1])
        scentWeigthPredator = self._search_predator_scent(predatorScentList, tile[0]) * 2

        return (tile[0],  (tileWeight - scentWeigthPredator))
        
    def _get_max_weight(self, predator, flower, map, phase):
        searchArea = self.search(self.get_sense // 2)
        mapSearchReturn = map.get_map_list(searchArea)
        flowerScentTrail = flower.get_scent().get_scent_trail(self.get_sense())
        predatorScentTrail = predator.get_scent().get_scent_trail(self.get_sense())

        maxWeight = ((-1,-1), -2000)
        if phase == 1:
            for i in mapSearchReturn:
                returnValue = self._searching_weight(i, predatorScentTrail, flowerScentTrail, flower.get_position())
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 2:
            for i in mapSearchReturn:
                returnValue = self._stalking_weight(i, predatorScentTrail, flowerScentTrail, flower.get_position())
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 3:
            for i in mapSearchReturn:
                returnValue = self._pursuit_weight(i, predatorScentTrail)
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
            self.energy_used()
            return self.pathfinding(maxWeight, map)
        else: return []
        
    def strugle(self, predator):
        energy = self.get_energy()
        predatorEnergy = predator.get_energy()

        if energy > predatorEnergy:
            randNum = random.randint(0, 10000)
            if randNum <= energy:
                self.substract_energy(randNum)
                return True

        return False
    
    # potentily add a movement timer that is based on the creatures speed


def tester():
    testPrey = Prey(10, 10, 10,10, (10,10))
    testMap = Map()
    testPredator = Animal(10, 10, 10,10, (15,10))

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



    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nStrugle')

    testPredator.energy_used()
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