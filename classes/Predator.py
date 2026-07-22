from Animal import Animal
import random
import math
from StaticMap import StaticMap

global debug
debug = False
class Predator(Animal):

    def __init__(self, huntingStrategy, evolutionChance, speed, stealth, stamina, sense, position):
        self._huntingStrategy = huntingStrategy.lower()
        self._evolutionChance = evolutionChance
        super().__init__(speed, stealth, stamina, sense, position)

    

    # Getters
    def get_hunting_strategy(self):
        return self._huntingStrategy
    
    def get_evolution_chance(self):
        return self._evolutionChance

    def get_ambush_range(self):
        return round(4*math.log(self.get_stealth()/2)+4)
    

    # Setters
    def set_evolution_chance(self, newEvolutionChance):
        if newEvolutionChance < 0 or newEvolutionChance > 100:
            raise ValueError("Evolution Chance can not be less then 0")
        self._evolutionChance = newEvolutionChance
    
    # Helper functions
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
    
    def _search_prey_scent(self, scentList, position):
        scentStrength = 100
        scentList.reverse()
        for i in scentList:
            if position in i:
                return scentStrength
            else:
                scentStrength -= 5
        return 0
    
    
    def _searching_weight(self, tile, preyScentList, targetPos):
        global debug
        tileWeight = self._searching_tile_weight(tile[1])
        scentWeigthPrey = self._search_prey_scent(preyScentList, tile[0])

        movementNoise = random.randint(-5,5)
        if debug == True:
            movementNoise = 0
        if tile[0] == targetPos: target = 100
        else: target = 0
        return (tile[0],  (tileWeight + scentWeigthPrey + movementNoise + target))
    
    def _stalking_weight(self, tile, preyScentList, targetPos):
        global debug
        tileWeight = self._stalking_tile_weight(tile[1])
        scentWeigthPrey = self._search_prey_scent(preyScentList, tile[0])
        movementNoise = random.randint(-5,5)
        if debug == True:
                    movementNoise = 0
        if tile[0] == targetPos: target = 100
        else: target = 0
        return (tile[0],  (tileWeight + scentWeigthPrey + movementNoise + target))
    
    def _pursuit_weight(self, tile, preyScentList):
        tileWeight = self._pursuit_tile_weight(tile[1])
        scentWeigthPrey = self._search_prey_scent(preyScentList, tile[0])


        return (tile[0],  (tileWeight + scentWeigthPrey))
    

    def _get_max_weight(self, prey, map, phase):
        searchArea = self.search(self.get_sense() // 2)
        mapSearchReturn = map.get_map_list(searchArea)
        preyScentTrail = prey.get_scent().get_scent_trail(self.get_sense())
        preyPosition = prey.get_position()

        maxWeight = ((-1,-1), -2000)
        if phase == 1:
            for i in mapSearchReturn:
                returnValue = self._searching_weight(i, preyScentTrail, preyPosition)
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 2:
            for i in mapSearchReturn:
                returnValue = self._stalking_weight(i, preyScentTrail, preyPosition)
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 3:
            for i in mapSearchReturn:
                returnValue = self._pursuit_weight(i, preyScentTrail)
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        return maxWeight



    def _evolve(self, stats):
        localCopy = stats.copy()
        statToChange = random.randint(2,5)
        changeDegree = random.randint(0,100)
        if changeDegree > 95:
            localCopy[statToChange] = localCopy[statToChange] + 5
        elif changeDegree > 80:
            localCopy[statToChange] = localCopy[statToChange] + 4
        elif changeDegree > 70:
            localCopy[statToChange] = localCopy[statToChange] + 3
        elif changeDegree > 60:
            localCopy[statToChange] = localCopy[statToChange] + 2
        elif changeDegree > 50:
            localCopy[statToChange] = localCopy[statToChange] + 1
        elif changeDegree > 40:
            localCopy[statToChange] = localCopy[statToChange] - 1
        elif changeDegree > 30:
            localCopy[statToChange] = localCopy[statToChange] - 2
        elif changeDegree > 20:
            localCopy[statToChange] = localCopy[statToChange] - 3
        elif changeDegree > 20:
            localCopy[statToChange] = localCopy[statToChange] - 3
        elif changeDegree > 5:
            localCopy[statToChange] = localCopy[statToChange] - 4
        else:
            localCopy[statToChange] = localCopy[statToChange] - 5

        if localCopy[statToChange] > 100:
            localCopy[statToChange] = 100

        return localCopy



    # Methods
    def get_move_list(self, prey, map, phase):
        '''
        phase is given as an int according to the table below

        searching phase = 1
        stalking phase = 2
        pursuit phase = 3
        '''
        if self.get_energy() >= 0:
            #potentily add a check for if how much enrgy is left to use and remove final points from list
            maxWeight = self._get_max_weight(prey, map, phase)
            self.energy_used()
            return self.pathfinding(maxWeight[0], map)



    def ambush_check(self, tile):
        if self.get_hunting_strategy() != 'ambush':
            return False
        
        predatorPosition = self.get_position()
        distance = abs(tile[0] - predatorPosition[0]) + abs(tile[1] - predatorPosition[0])
        ambushRange = self.get_ambush_range()
        if distance <= ambushRange:
            return True
        
    def ambush(self, prey, map):
        if self.get_hunting_strategy() != 'ambush':
            return False
        
        preyPosition = prey.get_position()
        ambushRange = self.get_ambush_range()
        if self.ambush_check(preyPosition):
            path = self.pathfinding(preyPosition, map)
        else:
            return False

        if path[-1][0] <= ambushRange:
            # cost of an ambush
            self.substract_energy(self.get_stealth() * 3)
            self.set_position(preyPosition)
            return True
        else:
            return False

    def reproduction(self):
        global debug
        numberOfKids = random.randint(0,2)
        if debug == True:
            numberOfKids = 2
        evolutionChance = self.get_evolution_chance()
        startingStats = [self.get_hunting_strategy(), evolutionChance, self.get_speed(), self.get_stealth(), self.get_stamina(), self.get_sense()]
        kids = []
        for i in range(numberOfKids):
            newStats = startingStats
            if random.randint(0,100) < evolutionChance or debug == True:
                # chance to mutate up to 3 times
                numberOfMutations = random.randint(0,100)
                newStats = self._evolve(newStats)
                if numberOfMutations >= 50:
                    newStats = self._evolve(newStats)
                if numberOfMutations >= 99:
                    newStats = self._evolve(newStats)
            kids.append(Predator(newStats[0], newStats[1], newStats[2], newStats[3], newStats[4], newStats[5], (0,0)))
        return kids

        
        

        

def tester():
    global debug
    debug = True
    testPredator = Predator('ambush', 10, 40, 40, 40, 40, (42,35))
    testPrey = Animal(40, 40, 40, 40, (45, 30))
    testMap = StaticMap()

     #getters 
    print('Getters')

    if testPredator.get_hunting_strategy() == 'ambush':
            print('hunting strategy: pass')
    else:
        print('hunting strategy: fail')

    if testPredator.get_evolution_chance() == 10:
        print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    if testPredator.get_ambush_range() == 16:
        print('ambush range: pass')
    else:
        print('ambush range: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters 
    print('Setters')
    testPredator.set_evolution_chance(30)
    if testPredator.get_evolution_chance() == 30:
            print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    print('---------------------------------------------------------------------------------------------------------------------')
    
    #setters errors
    print('\nSetters Errors')


    try:
        testPredator.set_evolution_chance(-1)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        testPredator.set_evolution_chance(101)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    print('---------------------------------------------------------------------------------------------------------------------')
 
    print('Setters edge cases')
    testPredator.set_evolution_chance(0)
    if testPredator.get_evolution_chance() == 0:
            print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    testPredator.set_evolution_chance(100)
    if testPredator.get_evolution_chance() == 100:
            print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    testPredator.set_evolution_chance(30)

    print('---------------------------------------------------------------------------------------------------------------------')
    #methods 
    print('Get Move List')

    # Add more tests to cover risks

    print('\nPhase 1 (searching) test')

    # stuck on how to test a function with randomness built in.


    testMoveList = testPredator.get_move_list(testPrey, testMap, 1)
    exampleMoveList = [(1, (42, 35)), (2, (42, 34)), (3, (42, 33)), (4, (43, 33)), (5, (43, 32)), (6, (43, 31)), (7, (43, 30)), (9, (44, 30)), (10, (45, 30))]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 2 (Stalking) test')
    testMoveList = testPredator.get_move_list(testPrey, testMap, 2)
    exampleMoveList = [(1, (42, 35)), (2, (42, 34)), (3, (42, 33)), (4, (43, 33)), (5, (43, 32)), (6, (43, 31)), (7, (43, 30)), (9, (44, 30)), (10, (45, 30))]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 3 (pursuit) test')
    testMoveList = testPredator.get_move_list(testPrey, testMap, 3)
    exampleMoveList = [(1, (42, 35)), (2, (42, 36)), (3, (42, 37)), (4, (43, 37)), (5, (43, 38)), (6, (43, 39)), (7, (43, 40)), (8, (43, 41)), (10, (43, 42)), (11, (42, 42))]
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag and testMap.get_map_point((25,26))[1] == 3:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('---------------------------------------------------------------------------------------------------------------------')
    print('Check ambush')

    if testPredator.ambush_check((45, 30)):
        print('ambush check: pass')
    else:
        print('ambush check: false')

    # check out of range
    if not testPredator.ambush_check((145, 30)):
        print('ambush check: pass')
    else:
        print('ambush check: false')

    print('---------------------------------------------------------------------------------------------------------------------')
    print('Reproduction')
    kids = testPredator.reproduction()
    for i in kids:
        if (i.get_hunting_strategy() == testPredator.get_hunting_strategy() and i.get_evolution_chance() == testPredator.get_evolution_chance()) and (i.get_speed() != testPredator.get_speed() or i.get_stealth() != testPredator.get_stealth() or i.get_stamina() != testPredator.get_stamina() or i.get_sense() != testPredator.get_sense()) and i.get_position() == (0,0):
            print('reproduction: pass')
        else:
            print('reproduction: false')
        


if __name__ == '__main__':
    tester()
