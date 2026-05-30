import random

class Map:
    '''
    tiles look up
    --------------
    plain tile = 1
    tree tile = 2
    bush tile = 3
    '''
    _instance = None
    _MAPSCALE = 1000

    
    def _create_map(self):
        '''
        Map %
        60% plain tiles
        20% tree tiles
        20% bush tiles
        '''
        #adds + 1 to complete the grid 0 to _MAPSCALE instead of _MAPSCALE - 1
        for x in range(self._MAPSCALE + 1):
            self._map.append([])
            for y in range(self._MAPSCALE + 1):
                randNum = random.randint(0,100)
                if randNum >= 40:
                    self._map[x].append(1)
                elif randNum >= 20:
                    self._map[x].append(2)
                else:
                    self._map[x].append(3)



    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
            self._map = []
            self._create_map(self)

        return self._instance

    def get_x(self, xRow):
        return self._map[xRow].copy()
    
    def get_y(self, yColumn):
        returnArray = []
        for i in self._map:
            returnArray.append(i[yColumn])
        return returnArray
    
    def get_map_list(self, pointList):
        '''
        expects point list as a list of tuples in the form (x,y)
        '''
        returnArray = []
        for point in pointList:
            #error checking
            returnArray.append((point,self._map[point[0]][point[1]]))
        
        return returnArray




    
    

def tester():
    map1 = Map()

    print('---------------------------------------------------------------------------------------------------------------------')

    print('Map Size test')

    if len(map1._map) == map1._MAPSCALE + 1:
        print('Map Size X Scale: pass')
    else:
        print('Map Size X Scale: fail')

    
    testFlag = True
    for i in map1._map:
        if len(i) != map1._MAPSCALE + 1:
            testFlag = False

    if testFlag:
        print('Map Size Y Scale: pass')
    else:
        print('Map Size Y Scale: fail')
    
    print('---------------------------------------------------------------------------------------------------------------------')
    print('Map Tile Distribution test')


    plainCount = 0
    treeCount = 0
    bushCount = 0
    totalCount = 0
    for i in map1._map:
        for t in i:
            if t == 1: plainCount += 1
            elif t == 2: treeCount += 1
            else: bushCount += 1

            totalCount += 1
    
    if round(plainCount / totalCount, 2) == 0.60:
        print('Map Plain tile Distribution: pass')
    else:
        print('Map Plain tile Distribution: fail')

    if round(treeCount / totalCount, 2) == 0.20:
        print('Map Tree tile Distribution: pass')
    else:
        print('Map Tree tile Distribution: fail')

    if round(bushCount / totalCount, 2) == 0.20:
        print('Map Bush tile Distribution: pass')
    else:
        print('Map Bush tile Distribution: fail')

    print('---------------------------------------------------------------------------------------------------------------------')
    print('Map Getters test')

    testSample = map1.get_x(9)
    if testSample == map1._map[9]:
        print('Map Get X: pass')
    else:
        print('Map Get X: fail')

    testSample = map1.get_y(9)
    exampleArray = []
    for i in map1._map:
        exampleArray.append(i[9])

    if testSample == exampleArray:
        print('Map Get Y: pass')
    else:
        print('Map Get Y: fail')

    testPoints = [(9,1), (10,2), (100, 43), (14, 46), (57,32), (33, 88), (87, 93), (55, 55), (49, 69), (31, 80)]
    testSample = map1.get_map_list(testPoints)
    
    testFlag = True
    for i in range(len(testPoints)):
        if testPoints[i] != testSample[i][0]:
            testFlag = False
        

    if testFlag:
        print('Map Get List: pass')
    else:
        print('Map Get List: fail')

    print('---------------------------------------------------------------------------------------------------------------------')
    print('Map Singleton test')
    # has a 1.6935087808430286711036596724754e-5% = (1/3)^10 chance of working without being a singleton 
    testPoints = [(9,1), (10,2), (100, 43), (14, 46), (57,32), (33, 88), (87, 93), (55, 55), (49, 69), (31, 80)]
    testSample1 = map1.get_map_list(testPoints)

    map2 = Map()
    testSample2 = map2.get_map_list(testPoints)

    if testSample1 == testSample2:
        print('Map ingleton: pass')
    else:
        print('Map ingleton: fail')


    
    

if __name__ == '__main__':
    tester()