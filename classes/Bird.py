from Prey import Prey
import heapq
import math

class Bird(Prey):

    def __init__(self, speed, stealth, stamina, sense, position):
        self._inAir = False
        super().__init__(speed, stealth, stamina, sense, position)


    #Helper functions
    def _cellWeight(self, point, map):
        checkMap = map.get_map_point(point)
        if checkMap[1] == 1:
            return 1
        if checkMap[1] == 2:
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
        self._inAir = newValue

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
                # removed check for trees
                if new_pos not in searched_list:
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
    





def tester():
    pass


if __name__ == '__main__':
        tester()