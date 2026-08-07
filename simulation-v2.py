#imports
import random as r
import argparse
import concurrent.futures
import pandas as pd

from classes.Predator import Predator
from classes.Rabbit import Rabbit
from classes.Bird import Bird
from classes.Mouse import Mouse
from classes.Plant import Plant
from classes.Map import Map


#set up vars
map = Map()





#helper methods
def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def seroundingTilesCheck(position, map, debug = False):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if debug: print(map.get_map_point(position))
    countTrees = 0
    for dir in directions:
        newPos = map.get_map_point((position[0] + dir[0], position[1] + dir[1]))
        if debug: print(map.get_map_point((position[0] + dir[0], position[1] + dir[1])))
        if newPos is None or newPos[1] == 2:
            countTrees += 1
        
    if countTrees >= 2: return False
    else: return True





#Sim methods
def placeAnimals(predator, prey, plants, map, debug = False):
    preyInPlace = False
    predatorInPlace = False
    p1Inplace = False
    p2Inplace = False
    p3Inplace = False
    p4Inplace = False
    mapLimit = map.get_map_limit()
    
    while not (preyInPlace and predatorInPlace and p1Inplace and p2Inplace and p3Inplace and p4Inplace):
        if not predatorInPlace:
            predator.set_position((r.randint(1,mapLimit),r.randint(1,mapLimit)))
        if not preyInPlace:
            prey.set_position((r.randint(1,mapLimit),r.randint(1,mapLimit)))
        if not p1Inplace:
            plants[0].set_position((r.randint(mapLimit // 3, mapLimit // 2),r.randint(mapLimit // 3, mapLimit // 2)))
        if not p2Inplace:
            plants[1].set_position((r.randint(mapLimit // 3, mapLimit // 2),r.randint(mapLimit // 3, mapLimit // 2)))
        if not p3Inplace:
            plants[2].set_position((r.randint(mapLimit // 3, mapLimit // 2),r.randint(mapLimit // 3, mapLimit // 2)))
        if not p4Inplace:
            plants[3].set_position((r.randint(mapLimit // 3, mapLimit // 2),r.randint(mapLimit // 3, mapLimit // 2)))
        if debug:
            print("predator = {} prey = {} p1 = {} p2 = {} p3 = {} p4 = {}".format(map.get_map_point(predator.get_position()), map.get_map_point(prey.get_position()), map.get_map_point(plants[0].get_position()), map.get_map_point(plants[1].get_position()), map.get_map_point(plants[2].get_position()), map.get_map_point(plants[3].get_position())))
        
        if map.get_map_point(predator.get_position())[1] != 2 and seroundingTilesCheck(predator.get_position(), map):
            predatorInPlace = True

        if map.get_map_point(prey.get_position())[1] != 2 and seroundingTilesCheck(prey.get_position(), map):
            preyInPlace = True

        if map.get_map_point(plants[0].get_position())[1] != 2 and seroundingTilesCheck(plants[0].get_position(), map):
            p1Inplace = True

        if map.get_map_point(plants[1].get_position())[1] != 2 and seroundingTilesCheck(plants[1].get_position(), map):
            p2Inplace = True

        if map.get_map_point(plants[2].get_position())[1] != 2 and seroundingTilesCheck(plants[2].get_position(), map):
            p3Inplace = True

        if map.get_map_point(plants[3].get_position())[1] != 2 and seroundingTilesCheck(plants[3].get_position(), map):
            p4Inplace = True

        if debug:
            print("predator = {} prey = {} p1 = {} p2 = {} p3 = {} p4 = {}".format(predatorInPlace, preyInPlace, p1Inplace, p2Inplace, p3Inplace, p4Inplace))




def movementCycle1(predator, prey, plants, map, phase, preyEating = False, debug = False):
    minDistance = map.get_map_limit() ** 3 # bigger then the map
    preyTarget = None
    for i in plants:
        if distance(i.get_position(), prey.get_position()) < minDistance:
            minDistance = distance(i.get_position(), prey.get_position())
            preyTarget = i

    #formula for finding movement speed to movment opertunities
    # translation graph https://www.desmos.com/calculator/yx1c7ib3lb
    preyMovementOpertunityMax = 80 // prey.speed_to_tiles()
    preyMovementOpertunity = preyMovementOpertunityMax
    predatorMovementOpertunityMax = 80 // predator.speed_to_tiles()
    predatorMovementOpertunity = predatorMovementOpertunityMax

    scentCountDownMax = 25 # will update 3 times per movement cycle
    scentCountDown = scentCountDownMax
    preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
    predatorMoveList = predator.get_move_list(prey, map, phase)

    for i in range(0,81):
        if debug:
            print('------------------------------------------------------------------------------------------------------------------------------------------')
            print(i)
            print('preyMoveList = {} \npreyMoveOpertunity = {} \npreyMoveMax = {} \npreyPosition = {}'.format(preyMoveList, preyMovementOpertunity, preyMovementOpertunityMax, prey.get_position(), prey.get_scent().get_scent_trail(100)))
            print()
            print('predatorMoveList = {} \npredatorMoveOpertunity = {} \npredatorMoveMax = {} \npredatorPosition = {}'.format(predatorMoveList, predatorMovementOpertunity, predatorMovementOpertunityMax, predator.get_position(), predator.get_scent().get_scent_trail(100)))
    
        if preyMovementOpertunity == 1 and prey.get_energy() >= 0 and not preyEating:
            preyMovementOpertunity = preyMovementOpertunityMax
            prey.set_position(preyMoveList[0])
            preyMoveList = preyMoveList [1:]
            if len(preyMoveList) == 0:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)

        else:
            preyMovementOpertunity -= 1
        if predatorMovementOpertunity == 1 and predator.get_energy() >= 0:
            predatorMovementOpertunity = predatorMovementOpertunityMax
            predator.set_position(predatorMoveList[0])
            predatorMoveList = predatorMoveList [1:]
            if len(predatorMoveList) == 0:
                predatorMoveList = predator.get_move_list(prey, map, phase)
        else:
            predatorMovementOpertunity -= 1

        if scentCountDown == 1:
            scentCountDown = scentCountDownMax
            prey.scent_decay()
            prey.update_scent_trail()
            predator.scent_decay()            
            predator.update_scent_trail()
            
        else:
            scentCountDown -= 1
        
def movementCycle2(predator, prey, plants, map, phase, preyType, stunned = False, debug = False):
    preyTarget = plants[0]

    #formula for finding movement speed to movment opertunities
    # translation graph https://www.desmos.com/calculator/yx1c7ib3lb
    if not stunned:
        preyMovementOpertunityMax = 80 // prey.speed_to_tiles() # change this here
        preyMovementOpertunity = preyMovementOpertunityMax
    predatorMovementOpertunityMax = 80 // predator.speed_to_tiles()
    predatorMovementOpertunity = predatorMovementOpertunityMax

    preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
    predatorMoveList = predator.get_move_list(prey, map, phase)

    for i in range(0,81):
        if debug:
            print('------------------------------------------------------------------------------------------------------------------------------------------')
            print(i)
            print('preyMoveList = {} \npreyMoveOpertunity = {} \npreyMoveMax = {} \npreyPosition = {} \npreyScent = {}'.format(preyMoveList, preyMovementOpertunity, preyMovementOpertunityMax, prey.get_position(), prey.get_scent().get_scent_trail(100)))
            print()
            print('predatorMoveList = {} \npredatorMoveOpertunity = {} \npredatorMoveMax = {} \npredatorPosition = {} \npredatorScent = {}'.format(predatorMoveList, predatorMovementOpertunity, predatorMovementOpertunityMax, predator.get_position(), predator.get_scent().get_scent_trail(100)))
        if not stunned and preyMovementOpertunity == 1 and prey.get_energy() >= 0 and preyType != 'bird':
            if preyType == 'rabbit' and map.get_map_point(prey.get_position())[0] == 3:
                return True
            preyMovementOpertunity = preyMovementOpertunityMax
            prey.set_position(preyMoveList[0])
            preyMoveList = preyMoveList [1:]
            prey.scent_decay()
            prey.update_scent_trail()

            if len(preyMoveList) == 0:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
            predatorMoveList = predator.get_move_list(prey, map, phase)
        elif not stunned:
            preyMovementOpertunity -= 1

        if predatorMovementOpertunity == 1 and predator.get_energy() >= 0:
            predatorMovementOpertunity = predatorMovementOpertunityMax
            predator.set_position(predatorMoveList[0])
            predatorMoveList = predatorMoveList [1:]
            predator.scent_decay()            
            predator.update_scent_trail()
            if len(predatorMoveList) == 0:
                predatorMoveList = predator.get_move_list(prey, map, phase)
            if not stunned:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
        else:
            predatorMovementOpertunity -= 1
    if preyType == 'bird' and distance(predator.get_position(), prey.get_position()) > 1 and not stunned:
        return True
    else:
        return False
            






def simulation(predator, prey, map):

    #set up objects
    r.seed()
    plants = [Plant((0,0)), Plant((0,0)), Plant((0,0)), Plant((0,0))]
    
    placeAnimals(predator, prey, plants, map)

    # sim vars
    eatingCyclesMax = 3
    eatingCyclesLeft = eatingCyclesMax
    eatingTarget = None
    eatingPlant = False
    succesfulStalk = False
    spotted = False
    preyCaught = False
    preyStrugle = False
    huntingStrategy = predator.get_hunting_strategy()
    preyType = prey.__class__.__name__
    preySence = prey.get_sense()
    predatorStealth = predator.get_stealth()

    # limit factors
    cycleCount = 0
    startDistance = distance(prey.get_position(), predator.get_position())


    # simulation
    while not prey.get_escaped() and predator.get_energy() >= 0 and not preyCaught and len(plants) > 0:
        cycleCount += 1
        if not spotted and not succesfulStalk:
            # phase 1 and 2
            if distance(prey.get_position(), predator.get_position()) > 100:
                movementCycle1(predator, prey, plants, map, 1, preyEating = eatingPlant)
                prey.energy_used()
                predator.energy_used()
                prey.update_scent_trail()
                predator.update_scent_trail()

            elif ((huntingStrategy == 'ambush' and not predator.ambush_check(prey.get_position())) or (huntingStrategy == 'pursuit' and distance(prey.get_position(), predator.get_position()) > predator.get_pursuit_range())): 
                movementCycle1(predator, prey, plants, map, 2, preyEating = eatingPlant)
                chance = (predatorStealth + (distance(prey.get_position(), predator.get_position()) * 3)) - preySence # 50 stealth leads to a min range of 26 distance for ambush. Thus 26 * 2 = 52 giving the predator a 52% maximum chance at 50 stealth vs 50 sense
                if chance < 100:
                    spotAttempt = r.randint(0,100)
                    if spotAttempt > chance:
                        spotted = True
                prey.energy_used()
                predator.energy_used()
                prey.update_scent_trail()
                predator.update_scent_trail()
            else:
                succesfulStalk = True


            if eatingPlant == False:
                preyPosition = prey.get_position()
                for p in plants:
                    plantPos = p.get_position()
                    if preyPosition == plantPos:
                        eatingPlant = True
                        eatingCyclesLeft = eatingCyclesMax
                        eatingTarget = p

            elif eatingPlant == True and eatingCyclesLeft == 0:
                eatingPlant = False
                plants.remove(eatingTarget)
            else:
                eatingCyclesLeft -= 1

        else:
            # phase 3 and 4
            if huntingStrategy == 'ambush' and predator.ambush_check(prey.get_position()) and not spotted:
                #phase 3 ambush
                predator.ambush(prey)
                killChance = predator.get_stealth() // 2
                randnum = r.randint(0,100)
                if randnum < killChance:
                    preyCaught = True
                else:
                    preyStrugle = True
                    spotted = True

            elif preyStrugle:
                # phase 4
                result = prey.strugle(predator)
                if not result:
                    preyCaught = True
                else:
                    predatorPos = predator.get_position()
                    notFoundPlace = True
                    countSearcharea = 4
                    newPos = None
                    while notFoundPlace:
                        mapList = prey.search(countSearcharea)
                        for currentPos in mapList:
                            if distance(currentPos, predatorPos) > 1 and seroundingTilesCheck(currentPos, map) and not map.get_map_point(currentPos)[0] == 2:
                                notFoundPlace = False
                                newPos = currentPos
                                break
                        countSearcharea += 1
                                                        
                    prey.set_position(newPos)
                    preyStrugle = False

            elif distance(predator.get_position(), prey.get_position()) <= 1:
                preyStrugle = True

            elif distance(predator.get_position(), prey.get_position()) > predator.get_pursuit_range():
                prey.set_escaped(True)

            elif not spotted:
                movementCycle2(predator, prey, plants, map, 3, preyType, stunned=True)
                prey.energy_used()
                predator.energy_used()

            else:
                #phase 3 pursuit
                prey.set_escaped(movementCycle2(predator, prey, plants, map, 3, preyType))
                prey.energy_used()
                predator.energy_used()
    if cycleCount == 0:
        cycleFromDis = startDistance
    else:
        cycleFromDis = startDistance / cycleCount
    if preyCaught:
        return (1, predator.reproduction(), preyType, cycleFromDis, predator.get_energy(), spotted)
    else:
        return (0, [predator], preyType, cycleFromDis, predator.get_energy(), spotted)

                     



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", type=str, help="Redirects the standard output into the designated file location")

    parser.add_argument("-sp", "--startingPopulation", type=str, help="Sets the starting population size (how many predators are in generation 0). Defult = 10,000. < 1000 is not recomended as population will likely go extinct")

    parser.add_argument("-g", "--generation", type=str, help="Sets how many generations the simulation will go through. Defult = 1,000.")

    parser.add_argument("-sm", "--startingMax", type=str, help="Sets the maximum for population size at the start (how many predators are allowed after generation 0). Defult = 5000. < 100 is not recomended as population will likely go extinct")

    parser.add_argument("-em", "--endingMax", type=str, help="Sets the maximum for population size at the end (how many predators are allowed in the final generation). Defult = 500.")
    

    args = parser.parse_args()

   




    if args.startingPopulation:
        sp = int(args.startingPopulation)
        if sp < 1:
            raise ValueError('startingPopulation can not be less then 1')
        else:
            startingPopulation = sp
    else:
        startingPopulation = 10000

    if args.generation:
        gen = int(args.generation)
        if gen < 0:
            raise ValueError('generation can not be less then 0')
        else:
            generations = gen
    else:
        generations = 100

    if args.startingMax:
        sm = int(args.startingMax)
        if sm < 1:
            raise ValueError('starting max can not be less then 1')
        else:
            startMaxPop = sm
    else:
        startMaxPop = 500 # starting maximum space of the population

    if args.endingMax:
        em = int(args.endingMax)
        if em < 1:
            raise ValueError('ending max can not be less then 1')
        else:
            endMaxPop = em
    else:
        endMaxPop = 100 # endding maximum space of the popuation
    
    
    decayAmount = 20
    diviser = (startMaxPop - endMaxPop) / decayAmount 
    rateOfDecay = (generations // diviser) // 2 # calculate the rate of decay to reach the final pop at half way through the simulation
    
    
    outputData = pd.DataFrame({
        'Generation': [],
        'Hunting Strategy': [],
        'Speed': [],
        'Stealth':[],
        'Stamina': [],
        'Sense': [],
        'Hunting Outcome': [],
        'Prey Type': [],
        'First Order Facter': [],
        'Second Order Facter': []

    })

    nextGen = []

    # test 1 with rabbits
    firstGen = [Predator('ambush', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    firstGenPursuit = [Predator('pursuit', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    
    firstGen.extend(firstGenPursuit) # should give an even mix of prdators
    prey = Rabbit(50, 20, 60, 50, (0,0)) # first test is agenst rabbits.

    decayTimer = rateOfDecay
    
    currentPop = startMaxPop # population size of the current generation

    with concurrent.futures.ProcessPoolExecutor() as executor:

        futures = [executor.submit(simulation, predator, prey, map) for predator in firstGen]
        

        # First generation
        tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[]

                                })
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                'Generation': [0],
                                                                'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                'Speed': [result[1][0].get_speed()],
                                                                'Stealth':[result[1][0].get_stealth()],
                                                                'Stamina': [result[1][0].get_stamina()],
                                                                'Sense': [result[1][0].get_sense()],
                                                                'Hunting Outcome': [result[0]],
                                                                'Prey Type': [result[2]],
                                                                'cycles':[result[3]],
                                                                'energyLeft':[result[4]],
                                                                'spoted':[result[5]],
                                                                'kids':[result[1]]
                                                            })], ignore_index=True) # store this info in a temp table.

        # keep only the relevent info for study
        columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
        outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
        nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()

        # assuming the first generation is under the population limmit to save runtime and help the population stabilize
        for idx, val in nextGenselcetion['kids'].items():
            nextGen.extend(val)

        #second gen onword
        for g in range(1, generations + 1):
            print('generation = {}, generation starting size = {}, curent population max = {}'.format(g, len(nextGen), currentPop))
            futures = [executor.submit(simulation, predators, prey, map) for predators in nextGen]
            nextGen = []
            tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[],
                                    'num of kids':[]
                                })
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                    'Generation': [g],
                                                                    'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                    'Speed': [result[1][0].get_speed()],
                                                                    'Stealth':[result[1][0].get_stealth()],
                                                                    'Stamina': [result[1][0].get_stamina()],
                                                                    'Sense': [result[1][0].get_sense()],
                                                                    'Hunting Outcome': [result[0]],
                                                                    'Prey Type': [result[2]],
                                                                    'cycles':[result[3]],
                                                                    'energyLeft':[result[4]],
                                                                    'spoted':[result[5]],
                                                                    'kids':[result[1]],
                                                                    'num of kids':[len(result[1])]
                                                                })], ignore_index=True) # store this info in a temp table. 

            # keep only the relevent info for study
            columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
            outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
            # only consider predators that caught prey
            nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()
            numOfKidsSum = nextGenselcetion['num of kids'].sum()
            if numOfKidsSum > currentPop:
                averageNumbOfKids = numOfKidsSum / len(nextGenselcetion) # should be 2 but is derived for above average cases
                # once a run is compleate calculate second order facters into weighted average for second order.
                nextGenselcetion['first order'] = (nextGenselcetion['Speed'] + nextGenselcetion['Stealth'] + nextGenselcetion['Stamina'] + nextGenselcetion['Sense']) / 4
                nextGenselcetion['spoted Convertion'] = nextGenselcetion['spoted'].astype(int)
                # finds the weighted average of these three terms to form a second order tie braker selection
                maxCycles = nextGenselcetion['cycles'].max()
                nextGenselcetion['second order'] = (nextGenselcetion['cycles'] / maxCycles) * 0.4 + (nextGenselcetion['energyLeft'] / prey.get_energy_total()) * 0.2 + nextGenselcetion['spoted Convertion'] * 0.4

                # select top n canadents from first and second order.
                if g < generations // 2:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order']).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Maximize the stat total while having the max weighted average
                else:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order'], ascending=[True,False]).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Minimize the stat total while having the max weighted average
                    
                                    
                for idx, val in topOfGen['kids'].items():
                    nextGen.extend(val)
            else:
                for idx, val in nextGenselcetion['kids'].items():
                    nextGen.extend(val)

            if decayTimer <= 1 and currentPop > endMaxPop:
                decayTimer = rateOfDecay
                currentPop -= decayAmount
            else:
                decayTimer -= 1

    if generations == 0:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(0, len(nextGen), currentPop))
    else:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(g, len(nextGen), currentPop))


    nextGen = []

    # test 2 with Mouse
    firstGen = [Predator('ambush', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    firstGenPursuit = [Predator('pursuit', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    
    firstGen.extend(firstGenPursuit) # should give an even mix of prdators
    prey = Mouse(60, 20, 95, 80, (0,0)) # second is tested ageinst mice

    decayTimer = rateOfDecay
    
    currentPop = startMaxPop # population size of the current generation

    with concurrent.futures.ProcessPoolExecutor() as executor:

        futures = [executor.submit(simulation, predator, prey, map) for predator in firstGen]
        

        # First generation
        tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[]

                                })
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                'Generation': [0],
                                                                'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                'Speed': [result[1][0].get_speed()],
                                                                'Stealth':[result[1][0].get_stealth()],
                                                                'Stamina': [result[1][0].get_stamina()],
                                                                'Sense': [result[1][0].get_sense()],
                                                                'Hunting Outcome': [result[0]],
                                                                'Prey Type': [result[2]],
                                                                'cycles':[result[3]],
                                                                'energyLeft':[result[4]],
                                                                'spoted':[result[5]],
                                                                'kids':[result[1]]
                                                            })], ignore_index=True) # store this info in a temp table.

        # keep only the relevent info for study
        columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
        outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
        nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()

        # assuming the first generation is under the population limmit to save runtime and help the population stabilize
        for idx, val in nextGenselcetion['kids'].items():
            nextGen.extend(val)

        #second gen onword
        for g in range(1, generations + 1):
            print('generation = {}, generation starting size = {}, curent population max = {}'.format(g, len(nextGen), currentPop))
            futures = [executor.submit(simulation, predators, prey, map) for predators in nextGen]
            nextGen = []
            tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[],
                                    'num of kids':[]
                                })
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                    'Generation': [g],
                                                                    'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                    'Speed': [result[1][0].get_speed()],
                                                                    'Stealth':[result[1][0].get_stealth()],
                                                                    'Stamina': [result[1][0].get_stamina()],
                                                                    'Sense': [result[1][0].get_sense()],
                                                                    'Hunting Outcome': [result[0]],
                                                                    'Prey Type': [result[2]],
                                                                    'cycles':[result[3]],
                                                                    'energyLeft':[result[4]],
                                                                    'spoted':[result[5]],
                                                                    'kids':[result[1]],
                                                                    'num of kids':[len(result[1])]
                                                                })], ignore_index=True) # store this info in a temp table. 

            # keep only the relevent info for study
            columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
            outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
            # only consider predators that caught prey
            nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()
            numOfKidsSum = nextGenselcetion['num of kids'].sum()
            if numOfKidsSum > currentPop:
                averageNumbOfKids = numOfKidsSum / len(nextGenselcetion) # should be 2 but is derived for above average cases
                # once a run is compleate calculate second order facters into weighted average for second order.
                nextGenselcetion['first order'] = (nextGenselcetion['Speed'] + nextGenselcetion['Stealth'] + nextGenselcetion['Stamina'] + nextGenselcetion['Sense']) / 4
                nextGenselcetion['spoted Convertion'] = nextGenselcetion['spoted'].astype(int)
                # finds the weighted average of these three terms to form a second order tie braker selection
                maxCycles = nextGenselcetion['cycles'].max()
                nextGenselcetion['second order'] = (nextGenselcetion['cycles'] / maxCycles) * 0.4 + (nextGenselcetion['energyLeft'] / prey.get_energy_total()) * 0.2 + nextGenselcetion['spoted Convertion'] * 0.4

                # select top n canadents from first and second order.
                if g < generations // 2:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order']).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Maximize the stat total while having the max weighted average
                else:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order'], ascending=[True,False]).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Minimize the stat total while having the max weighted average
                    
                                    
                for idx, val in topOfGen['kids'].items():
                    nextGen.extend(val)
            else:
                for idx, val in nextGenselcetion['kids'].items():
                    nextGen.extend(val)

            if decayTimer <= 1 and currentPop > endMaxPop:
                decayTimer = rateOfDecay
                currentPop -= decayAmount
            else:
                decayTimer -= 1

    if generations == 0:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(0, len(nextGen), currentPop))
    else:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(g, len(nextGen), currentPop))


    nextGen = []

    # test 3 birds
    firstGen = [Predator('ambush', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    firstGenPursuit = [Predator('pursuit', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0)) for i in range(startingPopulation // 2)]
    
    firstGen.extend(firstGenPursuit) # should give an even mix of prdators
    prey = prey = Bird(40, 10, 40, 30, (0,0)) # final test is agenst birds.

    decayTimer = rateOfDecay
    
    currentPop = startMaxPop # population size of the current generation

    with concurrent.futures.ProcessPoolExecutor() as executor:

        futures = [executor.submit(simulation, predator, prey, map) for predator in firstGen]
        

        # First generation
        tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[]

                                })
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                'Generation': [0],
                                                                'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                'Speed': [result[1][0].get_speed()],
                                                                'Stealth':[result[1][0].get_stealth()],
                                                                'Stamina': [result[1][0].get_stamina()],
                                                                'Sense': [result[1][0].get_sense()],
                                                                'Hunting Outcome': [result[0]],
                                                                'Prey Type': [result[2]],
                                                                'cycles':[result[3]],
                                                                'energyLeft':[result[4]],
                                                                'spoted':[result[5]],
                                                                'kids':[result[1]]
                                                            })], ignore_index=True) # store this info in a temp table.

        # keep only the relevent info for study
        columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
        outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
        nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()

        # assuming the first generation is under the population limmit to save runtime and help the population stabilize
        for idx, val in nextGenselcetion['kids'].items():
            nextGen.extend(val)

        #second gen onword
        for g in range(1, generations + 1):
            print('generation = {}, generation starting size = {}, curent population max = {}'.format(g, len(nextGen), currentPop))
            futures = [executor.submit(simulation, predators, prey, map) for predators in nextGen]
            nextGen = []
            tempDataframe = pd.DataFrame({
                                    'Generation': [],
                                    'Hunting Strategy': [],
                                    'Speed': [],
                                    'Stealth':[],
                                    'Stamina': [],
                                    'Sense': [],
                                    'Hunting Outcome': [],
                                    'Prey Type': [],
                                    'cycles':[],
                                    'energyLeft':[],
                                    'spoted':[],
                                    'kids':[],
                                    'num of kids':[]
                                })
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                tempDataframe = pd.concat([tempDataframe, pd.DataFrame({
                                                                    'Generation': [g],
                                                                    'Hunting Strategy': [result[1][0].get_hunting_strategy()],
                                                                    'Speed': [result[1][0].get_speed()],
                                                                    'Stealth':[result[1][0].get_stealth()],
                                                                    'Stamina': [result[1][0].get_stamina()],
                                                                    'Sense': [result[1][0].get_sense()],
                                                                    'Hunting Outcome': [result[0]],
                                                                    'Prey Type': [result[2]],
                                                                    'cycles':[result[3]],
                                                                    'energyLeft':[result[4]],
                                                                    'spoted':[result[5]],
                                                                    'kids':[result[1]],
                                                                    'num of kids':[len(result[1])]
                                                                })], ignore_index=True) # store this info in a temp table. 

            # keep only the relevent info for study
            columns_to_keep = ['Generation', 'Hunting Strategy', 'Speed', 'Stealth', 'Stamina', 'Sense', 'Hunting Outcome', 'Prey Type']
            outputData = pd.concat([outputData[columns_to_keep], tempDataframe[columns_to_keep]], ignore_index=True)
            # only consider predators that caught prey
            nextGenselcetion = tempDataframe[tempDataframe['Hunting Outcome'] == 1].copy()
            numOfKidsSum = nextGenselcetion['num of kids'].sum()
            if numOfKidsSum > currentPop:
                averageNumbOfKids = numOfKidsSum / len(nextGenselcetion) # should be 2 but is derived for above average cases
                # once a run is compleate calculate second order facters into weighted average for second order.
                nextGenselcetion['first order'] = (nextGenselcetion['Speed'] + nextGenselcetion['Stealth'] + nextGenselcetion['Stamina'] + nextGenselcetion['Sense']) / 4
                nextGenselcetion['spoted Convertion'] = nextGenselcetion['spoted'].astype(int)
                # finds the weighted average of these three terms to form a second order tie braker selection
                maxCycles = nextGenselcetion['cycles'].max()
                nextGenselcetion['second order'] = (nextGenselcetion['cycles'] / maxCycles) * 0.4 + (nextGenselcetion['energyLeft'] / prey.get_energy_total()) * 0.2 + nextGenselcetion['spoted Convertion'] * 0.4

                # select top n canadents from first and second order.
                if g < generations // 2:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order']).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Maximize the stat total while having the max weighted average
                else:
                    topOfGen = nextGenselcetion.sort_values(by=['first order', 'second order'], ascending=[True,False]).head(int(currentPop / averageNumbOfKids)) # devided by average to get a close aproximation of population size. Minimize the stat total while having the max weighted average
                    
                                    
                for idx, val in topOfGen['kids'].items():
                    nextGen.extend(val)
            else:
                for idx, val in nextGenselcetion['kids'].items():
                    nextGen.extend(val)

            if decayTimer <= 1 and currentPop > endMaxPop:
                decayTimer = rateOfDecay
                currentPop -= decayAmount
            else:
                decayTimer -= 1

    if generations == 0:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(0, len(nextGen), currentPop))
    else:
        print('Final generation = {}, Final generation size = {}, Final population max = {}'.format(g, len(nextGen), currentPop))






    try:
        if args.output:
            outputData.to_csv(args.output, index=False)
        else:
            outputData.to_csv('csv/output.csv', index=False)
    except PermissionError:
         print('permission denied to write to output file')
         outputData.to_csv('csv/output.txt', index=False)
        