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
    print(map1.get_map_list([(0,1),(5,5), (9,9)]))

    map2 = Map()
    print(map2.get_map_list([(0,1),(5,5), (9,9)]))

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
    
    print('plain average: ' + str(plainCount / totalCount))
    print('tree average: ' + str(treeCount / totalCount))
    print('bush average: ' + str(bushCount / totalCount))
    

if __name__ == '__main__':
    tester()