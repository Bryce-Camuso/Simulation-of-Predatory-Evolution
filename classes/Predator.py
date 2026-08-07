from .Animal import Animal
import random
import math
from .StaticMap import StaticMap

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
        return round(6*math.log(self.get_stealth()/2)+7)  # https://www.desmos.com/calculator/cmxrds2z42
    
    def get_pursuit_range(self):
        # https://www.desmos.com/calculator/as0pjg7ngm
        if self.get_hunting_strategy() == 'pursuit':
            return round(self.speed_to_tiles() * 1.5)
        else:
            return round(self.speed_to_tiles() / 2)
    

    # Setters
    def set_evolution_chance(self, newEvolutionChance):
        if newEvolutionChance < 0 or newEvolutionChance > 100:
            raise ValueError("Evolution Chance can not be less then 0")
        self._evolutionChance = newEvolutionChance
    
    # Helper functions
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
    
    
    def _searching_weight(self, tile, preyScentLookup, targetPos, movementNoise, midpoint):
        global debug
        tilePos, tileType = tile
        tileWeight = self._searching_tile_weight(tileType)
        scentWeigthPrey = preyScentLookup.get(tilePos, 0) * 2
        
        midpush = self._distance((midpoint,midpoint), tilePos) // 20


        #movementNoise = random.randint(-5,5)
        if debug == True:
            movementNoise = 0
        if tilePos == targetPos: target = 100
        else: target = 0
        return (tilePos,  ((tileWeight + scentWeigthPrey + movementNoise + target) - (midpush)))
    
    def _stalking_weight(self, tile, preyScentLookup, targetPos, movementNoise):
        global debug
        tilePos, tileType = tile
        tileWeight = self._stalking_tile_weight(tileType)
        scentWeigthPrey = preyScentLookup.get(tilePos, 0)
        #movementNoise = random.randint(-5,5)
        if debug == True:
                    movementNoise = 0
        if tilePos == targetPos: target = 100
        else: target = 0
        return (tilePos,  (tileWeight + scentWeigthPrey + movementNoise + target))
    
    def _pursuit_weight(self, tile, preyScentLookup):
        tilePos, tileType = tile
        tileWeight = self._pursuit_tile_weight(tileType)
        scentWeigthPrey = preyScentLookup.get(tilePos, 0)
        
        return (tilePos,  (tileWeight + scentWeigthPrey))
    

    def _get_max_weight(self, prey, map, phase):
        searchArea = self.search(self.get_sense() // 2)
        mapSearchReturn = map.get_map_list(searchArea)
        preyScentTrail = prey.get_scent().get_scent_trail(self.get_sense())
        preyPosition = prey.get_position()
        preyScentLookup = self._scent_list_lookup_builder(preyScentTrail)
        #distanceCal = self._distance
        

        maxWeight = ((-1,-1), -2000)
        if phase == 1:
            randomList = random.choices(range(-5, 5), k=len(mapSearchReturn))
            midpoint = map.get_map_limit() // 2
            for i in mapSearchReturn:
                returnValue = self._searching_weight(i, preyScentLookup, preyPosition, randomList[-1], midpoint)
                randomList.pop()
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 2:
            randomList = random.choices(range(-5, 5), k=len(mapSearchReturn))
            for i in mapSearchReturn:
                returnValue = self._stalking_weight(i, preyScentLookup, preyPosition, randomList[-1])
                randomList.pop()
                if returnValue[1] > maxWeight[1]:
                    maxWeight = returnValue
        if phase == 3:
            for i in mapSearchReturn:
                returnValue = self._pursuit_weight(i, preyScentLookup)
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
        if localCopy[statToChange] < 1:
            localCopy[statToChange] = 1

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
            return self.pathfinding(maxWeight[0], map)
        else: return []


    def ambush_check(self, tile):
        if self.get_hunting_strategy() != 'ambush':
            return False
        
        predatorPosition = self.get_position()
        distance = self._distance(tile, predatorPosition)
        ambushRange = self.get_ambush_range()
        if distance <= ambushRange:
            return True
        
    def ambush(self, prey):
        if self.get_hunting_strategy() != 'ambush':
            return False
        
        preyPosition = prey.get_position()
        if self.ambush_check(preyPosition):
            pass
        else:
            return False

        
        # cost of an ambush
        self.substract_energy(self.get_stealth() * 3)
        self.set_position(preyPosition)
        return True

    def reproduction(self):
        global debug
        numberOfKids = random.randint(0,2)
        if debug == True:
            numberOfKids = 2
        evolutionChance = self.get_evolution_chance()
        startingStats = [self.get_hunting_strategy(), evolutionChance, self.get_speed(), self.get_stealth(), self.get_stamina(), self.get_sense()]
        kids = [Predator(startingStats[0], startingStats[1], startingStats[2], startingStats[3], startingStats[4], startingStats[5], (0,0))] # returns a fresh copy of the class to represent intself.
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
    testPredatorA = Predator('ambush', 10, 50, 50, 50, 50, (42,35))
    testPredatorP = Predator('pursuit', 10, 50, 50, 50, 50, (42,35))
    testPrey = Animal(40, 40, 40, 40, (45, 30))
    testMap = StaticMap()

     #getters 
    print('Getters')

    if testPredatorA.get_hunting_strategy() == 'ambush':
            print('hunting strategy: pass')
    else:
        print('hunting strategy: fail')

    if testPredatorA.get_evolution_chance() == 10:
        print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    if testPredatorA.get_ambush_range() == 26:
        print('ambush range: pass')
    else:
        print('ambush range: fail')

    if testPredatorP.get_pursuit_range() == 46:
        print('pursuit range (pursuit): pass')
    else:
        print('pursuit range (pursuit): fail')

    if testPredatorA.get_pursuit_range() == 16:
        print('pursuit range (ambush): pass')
    else:
        print('pursuit range (ambush): fail')
    print('---------------------------------------------------------------------------------------------------------------------')

    #setters 
    print('Setters')
    testPredatorA.set_evolution_chance(30)
    if testPredatorA.get_evolution_chance() == 30:
        print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    print('---------------------------------------------------------------------------------------------------------------------')
    
    #setters errors
    print('\nSetters Errors')


    try:
        testPredatorA.set_evolution_chance(-1)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        testPredatorA.set_evolution_chance(101)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    print('---------------------------------------------------------------------------------------------------------------------')
 
    print('Setters edge cases')
    testPredatorA.set_evolution_chance(0)
    if testPredatorA.get_evolution_chance() == 0:
            print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    testPredatorA.set_evolution_chance(100)
    if testPredatorA.get_evolution_chance() == 100:
            print('evolution chance: pass')
    else:
        print('evolution chance: fail')

    testPredatorA.set_evolution_chance(30)

    print('---------------------------------------------------------------------------------------------------------------------')
    #methods 
    print('Get Move List')

    # Add more tests to cover risks

    print('\nPhase 1 (searching) test')

    # stuck on how to test a function with randomness built in.


    testMoveList = testPredatorA.get_move_list(testPrey, testMap, 1)
    exampleMoveList = [(42, 35), (42, 34), (42, 33), (43, 33), (43, 32), (43, 31), (43, 30), (44, 30), (45, 30)]
    
    testFlag = False
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 2 (Stalking) test')
    testMoveList = testPredatorA.get_move_list(testPrey, testMap, 2)
    exampleMoveList = [(42, 35), (42, 34), (42, 33), (43, 33), (43, 32), (43, 31), (43, 30), (44, 30), (45, 30)]
    testFlag = False
    
    for i in range(len(exampleMoveList)):
        if exampleMoveList[i] == testMoveList[i]:
            testFlag = True

    if testFlag:
        print('Move List: pass')
    else:
        print('Move List: false')

    print('\nPhase 3 (pursuit) test')
    testMoveList = testPredatorA.get_move_list(testPrey, testMap, 3)
    exampleMoveList = [(42, 35), (42, 36), (42, 37), (43, 37), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (42, 42)]
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

    if testPredatorA.ambush_check((45, 30)):
        print('ambush check: pass')
    else:
        print('ambush check: false')

    # check out of range
    if not testPredatorA.ambush_check((145, 30)):
        print('ambush check: pass')
    else:
        print('ambush check: false')

    print('---------------------------------------------------------------------------------------------------------------------')
    print('Reproduction')
    kids = testPredatorA.reproduction()
    parent = kids[0]
    kids = kids[1:]
    if (parent.get_hunting_strategy() == testPredatorA.get_hunting_strategy() and parent.get_evolution_chance() == testPredatorA.get_evolution_chance()) and (parent.get_speed() == testPredatorA.get_speed() and parent.get_stealth() == testPredatorA.get_stealth() and parent.get_stamina() == testPredatorA.get_stamina() and parent.get_sense() == testPredatorA.get_sense()) and parent.get_position() == (0,0):
        print('reproduction: pass')
    else:
        print('reproduction: false')
        
    for i in kids:
        if (i.get_hunting_strategy() == testPredatorA.get_hunting_strategy() and i.get_evolution_chance() == testPredatorA.get_evolution_chance()) and (i.get_speed() != testPredatorA.get_speed() or i.get_stealth() != testPredatorA.get_stealth() or i.get_stamina() != testPredatorA.get_stamina() or i.get_sense() != testPredatorA.get_sense()) and i.get_position() == (0,0):
            print('reproduction: pass')
        else:
            print('reproduction: false')
        


if __name__ == '__main__':
    tester()
