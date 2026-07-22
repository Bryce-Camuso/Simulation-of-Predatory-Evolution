from Animal import Animal
import random


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
    

    # Setters
    def set_evolution_chance(self, newEvolutionChance):
        if newEvolutionChance < 0:
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
        tileWeight = self._searching_tile_weight(tile[1])
        scentWeigthPrey = self._search_prey_scent(preyScentList, tile[0])

        movementNoise = random.randint(-5,5)
        if tile[0] == targetPos: target = 100
        else: target = 0
        return (tile[0],  (tileWeight + scentWeigthPrey + movementNoise + target))
    
    def _stalking_weight(self, tile, preyScentList, targetPos):
        tileWeight = self._stalking_tile_weight(tile[1])
        scentWeigthPrey = self._search_prey_scent(preyScentList, tile[0])
        movementNoise = random.randint(-5,5)
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
        
    def ambush(self, prey):
        if self.get_hunting_strategy() != 'ambush':
            return False
        
        preyPosition = prey.get_position()
        predatorPosition = self.get_position()
        distance = abs(preyPosition[0] - predatorPosition[0]) + abs(preyPosition[1] - predatorPosition[0])
        print(distance)

        

def tester():
    testpredator = Predator('ambush', 10, 40, 40, 40, 40, (40,40))
    testPrey = Animal(40, 40, 40, 40, (45,35))

    testpredator.ambush(testPrey)

        


if __name__ == '__main__':
    tester()
