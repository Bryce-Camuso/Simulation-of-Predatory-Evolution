from Scent import Scent
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
        self._ENERGYTOTAL = 100
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
        self._speed = newSpeed

    def set_stealth(self, newStealth):
        self._stealth = newStealth

    def set_stamina(self, newStamina):
        self._stamina = newStamina

    def set_sense(self, newSense):
        self._sense = newSense

    def set_position(self, newPosition):
        self._position = newPosition

    def substract_energy(self, usedEnergy):
        self._energyLeft = self._energyLeft - usedEnergy




    # Helper functions
    def _get_stealth_percent(self, level):
        return 100 - (level * 25) - ((self.get_stealth() // 10) * 5)
    
    def _get_stealth_percent_string(self, level):
        return str(self._get_stealth_percent(level)) + '%'
    
    def _scent_search_top(self, position, level):
        #adds current position to array. Recursively searchs positions above itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1))
        return returnArray
    
    def _scent_search_right(self, position, level):
        #adds current position to array. Recursively searchs positions above, to it's right, and under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1))
        returnArray.extend(self._scent_search_right((position[0] + 1, position[1]), level + 1))
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1))
        return returnArray
    
    def _scent_search_bottom(self, position, level):
        #adds current position to array. Recursively searchs positions under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level), position)]
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1))

        return returnArray

    def _scent_search_left(self, position, level):
        #adds current position to array. Recursively searchs positions above, to it's left, and under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1))
        returnArray.extend(self._scent_search_left((position[0] - 1, position[1]), level + 1))
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1))

        return returnArray

    # Methods
    def energy_used(self):
        #returns a number from the calcualtion made in the milestone 4
        pass

    def pathfinding(self):
        #milestone 4
        pass

    def update_scent_trail(self):
        scentTrail = []
        
        # step 1) grab position lable as level 0 scent
        startPosition = self.get_position()
        scentTrail.append((self._get_stealth_percent_string(0), startPosition))

        #step 2) grab 4 adjacent neighbours as level 1 scent and then recursively find next 2 levels ending at level 3
        scentTrail.extend(self._scent_search_top((startPosition[0], startPosition[1] + 1), 1))
        scentTrail.extend(self._scent_search_right((startPosition[0] + 1, startPosition[1]), 1))
        scentTrail.extend(self._scent_search_bottom((startPosition[0], startPosition[1] - 1), 1))
        scentTrail.extend(self._scent_search_left((startPosition[0] - 1, startPosition[1]), 1))
        
        self._scent.add_scent_trail(scentTrail)
    
    def scent_decay(self):
        self._scent.scent_decay()
    


def tester():
    tester1 = Animal(50,50,50,50,(10,10))

    tester1.update_scent_trail()
    print(tester1._scent.get_scent_trail(100))

    print('---------------------------')
    tester1.scent_decay()
    print(tester1._scent.get_scent_trail(100))
    print('---------------------------')

    tester1.set_position((10,12))
    tester1.update_scent_trail()
    print(tester1._scent.get_scent_trail(100))
    print('---------------------------')
    print(tester1.get_scent())


    



if __name__ == '__main__':
    tester()