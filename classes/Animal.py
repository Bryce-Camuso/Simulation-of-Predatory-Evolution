from Scent import Scent
from Map import Map
import heapq
import math
class Animal:

    def __init__(self, speed, stealth, stamina, sense, position):
        '''
        params
        ------
        speed = how fast the creature can move
        stealth = how close a creature can get without being detected
        stamina = how efficent the creature uses energy
        sense = how far creature can see/smell
        position = where the creature is on the grid in the form of (x, y)

        note all stats are on a range from 0-100
        
        intnal Vars
        -----------
        _speed
        _stealth
        _stamina
        _sense
        _position
        _scent = scent object to keep track of the scents created by the creature
        _energyLeft = how much energy the creature has left to use

        CONST
        -----
        _ENERGYTOTAL = the total amount of energy a creature gets per generation

        
        '''
        self._ENERGYTOTAL = 10000
        self._speed = speed
        self._stealth = stealth
        self._stamina = stamina
        self._sense = sense
        self._position = position
        self._sentTrail = []
        self._scent = Scent()
        self._energyLeft = self._ENERGYTOTAL


    # getters
    def get_speed(self):
        return self._speed
    
    def get_stealth(self):
        return self._stealth
    
    def get_stamina(self):
        return self._stamina
    
    def get_sense(self):
        return self._sense
    
    def get_position(self):
        return self._position
    
    def get_energy(self):
        return self._energyLeft
    
    def get_scent(self):
        return self._scent
    
    # setters
    
    def set_speed(self, newSpeed):
        if newSpeed < 1:
            raise ValueError('Speed can not be set below 1')
        self._speed = newSpeed

    def set_stealth(self, newStealth):
        if newStealth < 1:
            raise ValueError('Stealth can not be set below 1')
        self._stealth = newStealth

    def set_stamina(self, newStamina):
        if newStamina < 1:
            raise ValueError('Stamina can not be set below 1')
        self._stamina = newStamina

    def set_sense(self, newSense):
        if newSense < 1:
            raise ValueError('Sense can not be set below 1')
        self._sense = newSense

    def set_position(self, newPosition):
        if not isinstance(newPosition, tuple):
            raise TypeError('Position must be a tuple')
        if newPosition[0] < 0 or newPosition[1] < 0:
            raise ValueError('Position can not contain a negative value in the x or y plain')
        self._position = newPosition

    def substract_energy(self, usedEnergy):
        if usedEnergy < 0:
            raise ValueError('Substract Energy can not subtract a negative value')
        self._energyLeft = self._energyLeft - usedEnergy




    # Helper functions
    
    def _cellWeight(self, point, map):
        checkMap = map.get_map_point(point)
        if checkMap[1] == 1:
            return 1
        elif checkMap[1] == 3:
            return 2
        

    # Methods
    def energy_used(self):
        #returns a number from the calcualtion made in the milestone 4
        speed = self.get_speed()
        stamina = self.get_stamina()
        stealth = self.get_stealth()
        sense = self.get_sense()
        energyCalculation = sense + ((speed * 2) - stamina) + (stealth * 2)
        self.substract_energy(energyCalculation)

    def pathfinding(self):
        #milestone 4
        pass

    def update_scent_trail(self):
        self._scent.update_scent_trail(self.get_position(), self.get_stealth())


    def scent_decay(self):
        self._scent.scent_decay()


    def pathfinding(self, targetTile, map):
        speedToTiles = round(5*math.log(self.get_speed()/2)+5)
        position = self.get_position()

        #A* pathfinding https://www.geeksforgeeks.org/dsa/a-search-algorithm/
        
        queue = []
        queueList = {position: 0}
        heapq.heappush(queue, (0 ,position))
        searched_list = {position}
        paths = {}
        foundFlag = False


        while len(queue) > 0 and foundFlag == False:
            p = heapq.heappop(queue)
            searched_list.add(p[1])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in directions:
                new_pos = (p[1][0] + dir[0], p[1][1] + dir[1])
                if map.get_map_point(new_pos)[1] != 2 and new_pos not in searched_list:
                    if new_pos == targetTile:
                        g = self._cellWeight(new_pos, map)
                        h = abs(new_pos[0] - targetTile[0]) + abs(new_pos[1] - targetTile[1])
                        f = g + h
                        searched_list.add(new_pos)
                        paths.update({new_pos: p })
                        foundFlag = True
                    else:
                        g = self._cellWeight(new_pos, map)
                        h = abs(new_pos[0] - targetTile[0]) + abs(new_pos[1] - targetTile[1])
                        f = g + h
                        if new_pos in queueList:
                            if queueList[new_pos] > f:
                                paths.update({new_pos: (g, p[1]) })
                                queue.remove(new_pos)
                                heapq.heappush(queue, (f,new_pos))
                                queueList[new_pos] = f
                        else:
                            paths.update({new_pos: (g, p[1]) })
                            heapq.heappush(queue, (f,new_pos))
                            queueList.update({new_pos: f}) 


        currentNode = (g, targetTile)
        fullPath = [currentNode]
        while True:
            if currentNode[1] in paths:
                currentNode = paths[currentNode[1]]
                fullPath.append(currentNode)
            else: break
        fullPath.reverse()
        sum = 0
        for i in range(len(fullPath)):
            sum = fullPath[i][0] + sum
            if sum > speedToTiles:
                return fullPath[:i]
            else:
                fullPath[i] = (sum, fullPath[i][1])
        return fullPath
    


#self tester ------------------------------------------------------------------------------------------------------------------------------------------
def tester():
    test1 = Animal(20,20,20,20,(10,10))
    test2 = Animal(25,25,25,25,(30,30))
    test3 = Animal(100,100,100,100,(30,30))
    scentObj = Scent()
    #test set 1) getters and setters
    #getters
    print('Getters')
    if test1.get_speed() == 20:
        print('speed: pass')
    else:
        print('speed: fail')

    if test1.get_stealth() == 20:
        print('stealth: pass')
    else:
        print('stealth: fail')

    if test1.get_stamina() == 20:
        print('stamina: pass')
    else:
        print('stamina: fail')

    if test1.get_sense() == 20:
        print('sense: pass')
    else:
        print('sense: fail')

    if test1.get_position() == (10,10):
        print('position: pass')
    else:
        print('position: fail')

    if test1.get_energy() == 10000:
        print('energy: pass')
    else:
        print('energy: fail')

    if isinstance(test1.get_scent(), Scent):
        print('scent: pass')
    else:
        print('scent: fail')
    

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters
    print('\nSetters')

    test1.set_speed(50)
    if test1.get_speed() == 50:
        print('speed: pass')
    else:
        print('speed: fail')
    
    test1.set_stealth(50)
    if test1.get_stealth() == 50:
        print('stealth: pass')
    else:
        print('stealth: fail')

    test1.set_stamina(50)
    if test1.get_stamina() == 50:
        print('stamina: pass')
    else:
        print('stamina: fail')

    test1.set_sense(50)
    if test1.get_sense() == 50:
        print('sense: pass')
    else:
        print('sense: fail')

    test1.set_position((30,30))
    if test1.get_position() == (30,30):
        print('position: pass')
    else:
        print('position: fail')
    test1.substract_energy(10)
    if test1.get_energy() == 9990:
        print('energy: pass')
    else:
        print('energy: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters errors
    print('\nSetters')
    try:
        test1.set_speed(0)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        test1.set_stealth(0)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')
    
    try:
        test1.set_stamina(0)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        test1.set_sense(0)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        test1.set_position(0)
        print('Error: None')
    except TypeError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')
    
    try:
        test1.set_position((-1,0))
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')   

    try:
        test1.set_position((0,-1))
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')   

    try:
        test1.substract_energy(-1)
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')
        

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters valid edge cases
    print('\nSetters valid edge cases')
    
    test1.set_speed(1)
    if test1.get_speed() == 1:
        print('speed: pass')
    else:
        print('speed: fail')
    
    test1.set_stealth(1)
    if test1.get_stealth() == 1:
        print('stealth: pass')
    else:
        print('stealth: fail')

    test1.set_stamina(1)
    if test1.get_stamina() == 1:
        print('stamina: pass')
    else:
        print('stamina: fail')

    test1.set_sense(1)
    if test1.get_sense() == 1:
        print('sense: pass')
    else:
        print('sense: fail')

    test1.set_position((0,0))
    if test1.get_position() == (0,0):
        print('position: pass')
    else:
        print('position: fail')
    test1.substract_energy(0)
    if test1.get_energy() == 9990:
        print('energy: pass')
    else:
        print('energy: fail')

    print('---------------------------------------------------------------------------------------------------------------------')
    #test set 2) methods
    print('\nUpdate Scent Trail')

    print('\nstealth = 50 [-25% per level]')
    scentObj = Scent()
    test1.set_position((30,30))
    test1.set_stealth(50)
    test1.update_scent_trail()
    scentObj.update_scent_trail((30,30), 50)

    testFlag = True
    testScent = test1.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')
    print('\nChange position to (30,31) [test y movement]')
    test1.set_position((30,31))
    test1.update_scent_trail()
    scentObj.update_scent_trail((30,31), 50)

    testFlag = True
    testScent = test1.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')

    print('\nChange position to (31,30) [test x movement]')
    test1.set_position((31,30))
    test1.update_scent_trail()
    scentObj.update_scent_trail((31,30), 50)

    testFlag = True
    testScent = test1.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nstealth = 25 [-10% per level]')

    scentObj = Scent()
    test2.update_scent_trail()
    scentObj.update_scent_trail((30,30), 25)

    testFlag = True
    testScent = test2.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')
    print('\nChange position to (30,31) [test y movement]')
    test2.set_position((30,31))
    test2.update_scent_trail()
    scentObj.update_scent_trail((30,31), 25)

    testFlag = True
    testScent = test2.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')

    print('\nChange position to (31,30) [test x movement]')
    test2.set_position((31,30))
    test2.update_scent_trail()
    scentObj.update_scent_trail((31,30), 25)

    testFlag = True
    testScent = test2.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')


    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nstealth = 100 [-50% per level]')
    scentObj = Scent()
    test3.update_scent_trail()
    scentObj.update_scent_trail((30,30), 100)

    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')
    print('\nChange position to (30,31) [test y movement]')
    test3.set_position((30,31))
    test3.update_scent_trail()
    scentObj.update_scent_trail((30,31), 100)

    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')

    print('\nChange position to (31,30) [test x movement]')
    test3.set_position((31,30))
    test3.update_scent_trail()
    scentObj.update_scent_trail((31,30), 100)

    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')
    
    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nScent Decay')
    test3.scent_decay()
    scentObj.scent_decay()
    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Scent decay 1: pass')
    else:
        print('Scent decay 1: false')
        
    test3.scent_decay()
    scentObj.scent_decay()
    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i]  != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 2: pass')
    else:
        print('Scent decay 2: false')
    test3.scent_decay()
    scentObj.scent_decay()
    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 3: pass')
    else:
        print('Scent decay 3: false')

    test3.scent_decay()
    scentObj.scent_decay()
    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 4: pass')
    else:
        print('Scent decay 4: false')

    test3.scent_decay()
    scentObj.scent_decay()
    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Scent decay 5: pass')
    else:
        print('Scent decay 5: false')
    


    testFlag = True
    testScent = test3.get_scent().get_scent_trail(100)
    exampleObj = scentObj.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nEnergy Use')
    test4 = Animal(50,50,50,50,(50,50))

    test4.energy_used()

    if test4.get_energy() == 9800:
        print('Energy use: pass')
    else:
        print('Energy use: false')




    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nPathFinding')

    testMap = Map()
    testPoint = (45,45)
    # quick test to make sure point is reachable
    if testMap.get_map_point(testPoint)[1] != 2:
        pass
    else: testPoint = (55,55)

    testArray = test4.pathfinding(testPoint,testMap)
    if testArray[-1][1] == testPoint:
        print('PathFinding: pass')
    else:
        print('PathFinding: false')



if __name__ == '__main__':
        tester()