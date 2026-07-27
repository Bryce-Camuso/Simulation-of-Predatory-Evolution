import sys
import random as r
import math

sys.path.append('classes/')
from classes.Predator import Predator
from classes.Rabbit import Rabbit
from classes.Plant import Plant
from classes.Map import Map

map = Map()

predator = Predator('ambush', 10, r.randint(1,100), r.randint(1,100), r.randint(1,100), r.randint(1,100), (0,0))
prey = Rabbit(60, 20, 60, 40, (0,0))
plants = [Plant((0,0)), Plant((0,0)), Plant((0,0)), Plant((0,0))]

preyAlive = True
def placeAnimals(predator, prey, plants, map, debug = False):
    preyInPlace = False
    predatorInPlace = False
    p1Inplace = False
    p2Inplace = False
    p3Inplace = False
    p4Inplace = False
    
    while not (preyInPlace and predatorInPlace and p1Inplace and p2Inplace and p3Inplace and p4Inplace):
        if not predatorInPlace:
            predator.set_position((r.randint(1,1000),r.randint(1,1000)))
        if not preyInPlace:
            prey.set_position((r.randint(1,1000),r.randint(1,1000)))
        if not p1Inplace:
            plants[0].set_position((r.randint(1,1000),r.randint(1,1000)))
        if not p2Inplace:
            plants[1].set_position((r.randint(1,1000),r.randint(1,1000)))
        if not p3Inplace:
            plants[2].set_position((r.randint(1,1000),r.randint(1,1000)))
        if not p4Inplace:
            plants[3].set_position((r.randint(1,1000),r.randint(1,1000)))
        if debug:
            print("predator = {} prey = {} p1 = {} p2 = {} p3 = {} p4 = {}".format(map.get_map_point(predator.get_position()), map.get_map_point(prey.get_position()), map.get_map_point(plants[0].get_position()), map.get_map_point(plants[1].get_position()), map.get_map_point(plants[2].get_position()), map.get_map_point(plants[3].get_position())))
        
        if map.get_map_point(predator.get_position())[1] != 2:
            predatorInPlace = True

        if map.get_map_point(prey.get_position())[1] != 2:
            preyInPlace = True

        if map.get_map_point(plants[0].get_position())[1] != 2:
            p1Inplace = True

        if map.get_map_point(plants[1].get_position())[1] != 2:
            p2Inplace = True

        if map.get_map_point(plants[2].get_position())[1] != 2:
            p3Inplace = True

        if map.get_map_point(plants[3].get_position())[1] != 2:
            p4Inplace = True

        if debug:
            print("predator = {} prey = {} p1 = {} p2 = {} p3 = {} p4 = {}".format(predatorInPlace, preyInPlace, p1Inplace, p2Inplace, p3Inplace, p4Inplace))

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def movementCycle(predator, prey, plants, map, phase, updatePaths = False, debug = False):
    minDistance = 10000000 # bigger then the map
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

    preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
    predatorMoveList = predator.get_move_list(prey, map, phase)
    
    for i in range(0,61):
        if debug:
            print('------------------------------------------------------------------------------------------------------------------------------------------')
            print(i)
            print('preyMoveList = {} \npreyMoveOpertunity = {} \npreyMoveMax = {} \npreyPosition = {} \npreyScent = {}'.format(preyMoveList, preyMovementOpertunity, preyMovementOpertunityMax, prey.get_position(), prey.get_scent().get_scent_trail(100)))
            print()
            print('predatorMoveList = {} \npredatorMoveOpertunity = {} \npredatorMoveMax = {} \npredatorPosition = {} \npredatorScent = {}'.format(predatorMoveList, predatorMovementOpertunity, predatorMovementOpertunityMax, predator.get_position(), predator.get_scent().get_scent_trail(100)))
        if preyMovementOpertunity == 1 and prey.get_energy() >= 0:
            preyMovementOpertunity = preyMovementOpertunityMax
            prey.set_position(preyMoveList[0][1])
            preyMoveList = preyMoveList [1:]
            prey.scent_decay()
            prey.update_scent_trail()
            if len(preyMoveList) == 0:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
            if updatePaths:
                predatorMoveList = predator.get_move_list(prey, map, phase)
        else:
            preyMovementOpertunity -= 1
        if predatorMovementOpertunity == 1 and predator.get_energy() >= 0:
            predatorMovementOpertunity = predatorMovementOpertunityMax
            predator.set_position(predatorMoveList[0][1])
            predatorMoveList = predatorMoveList [1:]
            predator.scent_decay()
            predator.update_scent_trail()
            if len(predatorMoveList) == 0:
                predatorMoveList = predator.get_move_list(prey, map, phase)
            if updatePaths:
                preyMoveList = prey.get_move_list(predator, preyTarget, map, phase)
        else:
            predatorMovementOpertunity -= 1
    

placeAnimals(predator, prey, plants, map)

while not prey.get_escaped() and preyAlive and predator.get_energy() >= 0:
    if distance(prey.get_position(), predator.get_position()) > 100:
        # searching phase
        movementCycle(predator, prey, plants, map, 1)
        prey.energy_used()
        predator.energy_used()

    print('------------------------------------------------------------------------')
    print('predator position = {}'.format(predator.get_position()))
    print('predator energy = {}'.format(predator.get_energy()))
    print('prey position = {}'.format(prey.get_position()))
    print('prey energy = {}'.format(prey.get_energy()))