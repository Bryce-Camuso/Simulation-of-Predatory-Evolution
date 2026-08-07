from .Prey import Prey
from .StaticMap import StaticMap

class Bird(Prey):

    def __init__(self, speed, stealth, stamina, sense, position):
        self._inAir = False
        super().__init__(speed, stealth, stamina, sense, position)


    #Helper functions
    def _cellWeight(self, point, map):
        checkMap = map.get_map_point(point)
        if checkMap is None:
            return None
        elif checkMap[1] == 1:
            return 1
        elif checkMap[1] == 2:
            return 1
        elif checkMap[1] == 3:
            return 1
        
    def _searching_tile_weight(self, tileNum):
        if tileNum == 1:
            return 15
        if tileNum == 2:
            return 15
        if tileNum == 3:
            return 15
        
    def _stalking_tile_weight(self, tileNum):
        if tileNum == 1:
            return 15
        if tileNum == 2:
            return 20
        if tileNum == 3:
            return 20
        
    def _pursuit_tile_weight(self, tileNum):
        if tileNum == 1:
            return 20
        if tileNum == 2:
            return 20
        if tileNum == 3:
            return 50



    # Methods
    def get_in_air(self):
        return self._inAir
    
    def set_in_air(self, newValue):
        if not isinstance(newValue, bool):
            raise TypeError('New Value must be a bool type')
        self._inAir = newValue
    





def tester(): 
    testPrey = Bird(10, 10, 10, 10, (25,25))
    testMap = StaticMap()

    print('Getters')

    if testPrey.get_in_air() == False:
        print('in air: pass')
    else:
        print('in air: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters
    print('\nSetters')
    
    testPrey.set_in_air(True)
    if testPrey.get_in_air() == True:
        print('in air: pass')
    else:
        print('in air: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #setters errors
    print('\nSetters Errors')

    try:
        testPrey.set_in_air(0)
        print('Error: None')
    except TypeError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nPathfinding test')
    returnValue = testPrey.pathfinding((15,15), testMap)
    # testList = [(1, (25, 25)), (2, (24, 25)), (3, (23, 25)), (4, (22, 25)), (5, (21, 25)), (6, (20, 25)), (7, (19, 25)), (8, (18, 25)), (9, (17, 25)), (10, (16, 25)), (11, (15, 25)), (12, (15, 24)), (13, (15, 23))]
    checkOverTree = False
    for i in range(len(returnValue)):
        if returnValue[i] == (24, 25):
            checkOverTree = True

    if checkOverTree:
        print('pathfinding check: pass')
    else:
        print('pathfinding check: fail')

if __name__ == '__main__':
        tester()