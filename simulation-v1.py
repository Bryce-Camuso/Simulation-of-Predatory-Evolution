#imports
import sys
import random as r
import math
import time
import traceback
import argparse
import concurrent.futures
from functools import partial

sys.path.append('classes/')
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
    # translation graph https://www.desmos.com/calculator/h4c9voicdq
    preyMovementOpertunityMax = 60 // (round(5*math.log(prey.get_speed()/2)+5))
    preyMovementOpertunity = preyMovementOpertunityMax
    predatorMovementOpertunityMax = 60 // (round(5*math.log(predator.get_speed()/2)+5))
    predatorMovementOpertunity = predatorMovementOpertunityMax

    scentCountDownMax = 20
    scentCountDown = scentCountDownMax
    preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
    predatorMoveList = predator.get_move_list(prey, map, phase)

    preySence = prey.get_sense()
    predatorStealth = predator.get_stealth()
    
    for i in range(0,61):
        if debug:
            print('------------------------------------------------------------------------------------------------------------------------------------------')
            print(i)
            print('preyMoveList = {} \npreyMoveOpertunity = {} \npreyMoveMax = {} \npreyPosition = {} \npreyScent = {}'.format(preyMoveList, preyMovementOpertunity, preyMovementOpertunityMax, prey.get_position(), prey.get_scent().get_scent_trail(100)))
            print()
            print('predatorMoveList = {} \npredatorMoveOpertunity = {} \npredatorMoveMax = {} \npredatorPosition = {} \npredatorScent = {}'.format(predatorMoveList, predatorMovementOpertunity, predatorMovementOpertunityMax, predator.get_position(), predator.get_scent().get_scent_trail(100)))
        if preyMovementOpertunity == 1 and prey.get_energy() >= 0 and not preyEating:
            preyMovementOpertunity = preyMovementOpertunityMax
            prey.set_position(preyMoveList[0])
            preyMoveList = preyMoveList [1:]
            if len(preyMoveList) == 0:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
        elif phase == 2 and preyEating and preyMovementOpertunity == 1:
            preyMovementOpertunity = preyMovementOpertunityMax
            chance = (predatorStealth + distance(prey.get_position(), predator.get_position())) - preySence
            if chance < 100:
                spotAttempt = r.randint(0,100)
                if spotAttempt > chance:
                    return True
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
    return False
        
def movementCycle2(predator, prey, plants, map, phase, preyType, stunned = False, debug = False):
    preyTarget = plants[0]

    #formula for finding movement speed to movment opertunities
    # translation graph https://www.desmos.com/calculator/h4c9voicdq
    if not stunned:
        preyMovementOpertunityMax = 60 // (round(5*math.log(prey.get_speed()/2)+5))
        preyMovementOpertunity = preyMovementOpertunityMax
    predatorMovementOpertunityMax = 60 // (round(5*math.log(predator.get_speed()/2)+5))
    predatorMovementOpertunity = predatorMovementOpertunityMax

    preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
    predatorMoveList = predator.get_move_list(prey, map, phase)

    
    for i in range(0,61):
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
            







def simulation(predatorType, preyType, map):
    
    r.seed()
    # class refrences Rabbit(50, 20, 60, 60, (0,0)) Bird(60, 10, 40, 30, (0,0)) Mouse(60, 20, 95, 100, (0,0))
    if preyType == 'rabbit':
        prey = Rabbit(50, 20, 60, 60, (0,0))
    elif preyType == 'mouse':
            prey = Mouse(60, 20, 95, 100, (0,0))
    elif preyType == 'bird':
        prey = Bird(60, 10, 40, 30, (0,0))
    plants = [Plant((0,0)), Plant((0,0)), Plant((0,0)), Plant((0,0))]
    eatingCyclesMax = 3
    eatingCyclesLeft = eatingCyclesMax
    eatingTarget = None
    eatingPlant = False




    # simulation
    startTime = time.time()
    succsessSearchRate = 0
    succsessStalkRate = 0
    succsessSpotRate = 0
    preyEscapeRate = 0
    preyCatchRate = 0
    preyExhaustRate = 0
    predatorExhaustRate = 0
    succesfulPredators = []
    kids = []

    retries = 100
    try:    
        for count in range(retries):

            # reset vars
            if predatorType == 'ambush' or predatorType == 'pursuit':
                predator = Predator(predatorType, 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0))
            prey._energyLeft = prey._ENERGYTOTAL
            prey.set_escaped(False)
            plants = [Plant((0,0)), Plant((0,0)), Plant((0,0)), Plant((0,0))]
            eatingCyclesLeft = eatingCyclesMax
            eatingTarget = None
            eatingPlant = False
            placeAnimals(predator, prey, plants, map)


            # sim vars
            succesfulSearch = False
            succesfulStalk = False
            spotted = False
            preyCaught = False
            preyStrugle = False
            preyType = 'rabbit'
            huntingStrategy = predator.get_hunting_strategy()
            
            while not prey.get_escaped() and predator.get_energy() >= 0 and not preyCaught and len(plants) > 0:
                # print('predator position = {}'.format(predator.get_position()))
                # print('predator energy = {}'.format(predator.get_energy()))
                # print('prey position = {}'.format(prey.get_position()))
                # print('prey energy = {}'.format(prey.get_energy()))
                # print('eating Plat = {}'.format(eatingPlant))
                # print('------------------------------------------------------------------------')
                if not spotted and not succesfulStalk:
                    # phase 1 and 2
                    if distance(prey.get_position(), predator.get_position()) > 100:
                        movementCycle1(predator, prey, plants, map, 1, preyEating = eatingPlant)
                        prey.energy_used()
                        predator.energy_used()
                        prey.update_scent_trail()
                        predator.update_scent_trail()

                    elif ((huntingStrategy == 'ambush' and not predator.ambush_check(prey.get_position())) or (huntingStrategy == 'pursuit' and distance(prey.get_position(), predator.get_position()) > predator.get_pursuit_range())): 
                        spotted = movementCycle1(predator, prey, plants, map, 2, preyEating = eatingPlant)
                        succesfulSearch = True
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
                        killChance = predator.get_stealth()
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
                            
                            # movelist = prey.get_move_list(predator, plants[0],map,3)
                            # while len(movelist) >= 3:
                            #     print('test')
                            #     movelist = prey.get_move_list(predator, plants[0],map,3)
                            #     if len(movelist) >= 3:
                            #         prey.set_position(movelist[2])
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
                    #prey.set_escaped(True)


                    
            if succesfulSearch == True:
                succsessSearchRate += 1
            if succesfulStalk == True:
                succsessStalkRate += 1
            if spotted == True:
                succsessSpotRate += 1
            if prey.get_escaped() == True:
                preyEscapeRate += 1
            if preyCaught == True:
                preyCatchRate += 1
                returnList = predator.reproduction()
                succesfulPredators.append(returnList[0])
                if len(returnList) > 1:
                    kids.extend(returnList[1:])
            if predator.get_energy() <= 0:
                predatorExhaustRate += 1
            if prey.get_energy() <= 0 :
                preyExhaustRate += 1

            


    except:
        # print('predator position = {}'.format(predator.get_position()))
        # print('predator energy = {}'.format(predator.get_energy()))
        # print('prey position = {}'.format(prey.get_position()))
        # print('prey energy = {}'.format(prey.get_energy()))
        # print('------------------------------------------------------------------------')
        traceback.print_exc()

    finally:
        endTime = time.time()
        count += 1
        print('number of retries = {}'.format(retries))
        print('number of loops = {}'.format(count))
        print('predator type = {} prey type = {}'.format(huntingStrategy, preyType))
        print('total time = {} Average time = {}'.format(endTime - startTime, (endTime - startTime) / count))
        print(succsessSearchRate)
        print('success search rate = {}'.format(succsessSearchRate / count))
        print(succsessStalkRate)
        print('success stalk rate = {}'.format(succsessStalkRate / count))
        print(succsessSpotRate)
        print('success spot rate = {}'.format(succsessSpotRate / count))
        print((succsessSpotRate + succsessStalkRate))
        print('success phase 2 rate = {}'.format((succsessSpotRate + succsessStalkRate) / count))
        print(preyEscapeRate)
        print('escape rate = {}'.format(preyEscapeRate / count))
        print(preyCatchRate)
        print('catch rate = {}'.format(preyCatchRate / count))
        print(predatorExhaustRate)
        print('predator exhaust rate = {}'.format(predatorExhaustRate / count))
        print(preyExhaustRate)
        print('prey exhaust rate = {}'.format(preyExhaustRate / count))
        if count < 1000 and len(succesfulPredators) > 0:
            print('parents')
            for p in succesfulPredators:
                print('speed = {}, stealth = {}, stamina = {}, sense = {}'.format(p.get_speed(), p.get_stealth(), p.get_stamina(), p.get_sense()))
            print('------------------------------------------------------------------------')
            print('kids')
            for k in kids:
                print('speed = {}, stealth = {}, stamina = {}, sense = {}'.format(k.get_speed(), k.get_stealth(), k.get_stamina(), k.get_sense())) 
        





if __name__ == "__main__":
    startingPopulation = 5
    parser = argparse.ArgumentParser()

    parser.add_argument("predatorType", type=str, help="What predator type the simulation is using: Ambush | Pursuit")

    parser.add_argument("preyType", type=str, help="What prey type the simulation is using: Rabbit | Mouse | Bird")

    parser.add_argument("-o", "--output", type=str, help="Redirects the standard output into the designated file location")

    args = parser.parse_args()

    predatorType = args.predatorType.lower()
    preyType = args.preyType.lower()

    if args.output:
        sys.stdout = open(args.output, 'w')

    # optimized_worker = partial(process_data, constant_c=fixed_multiplier)

    # with concurrent.futures.ProcessPoolExecutor() as executor:

    #     futures = [executor.submit(simulation, predatorType, preyType, map) for _ in range(startingPopulation)]

    #     # futures = [executor.submit(greet_user, name, age, city="Chicago") for name, age in users] example for second gen on

    #     for future in concurrent.futures.as_completed(futures):
    #         result = future.result()
    #         print('------------------------------------------------------------------------')

    simulation(predatorType, preyType, map)

    sys.stdout.close()
    sys.stdout = sys.__stdout__
        