class Scent:

    def __init__(self):
        '''
        index look up
        0 = 5%
        1 = 10%
        2 = 15%
        3 = 20%
        4 = 25%
        5 = 30%
        6 = 35%
        7 = 40%
        8 = 45%
        9 = 50%
        10 = 55%
        11 = 60%
        12 = 65%
        13 = 70%
        14 = 75%
        15 = 80%
        16 = 85%
        17 = 90%
        18 = 95%
        19 = 100%

        scent stat lookup
        0 = >=100%
        5 = >=95%
        10 = >=90%
        15 = >=85%
        20 = >=80%
        25 = >=75%
        30 = >=70%
        35 = >=65%
        40 = >=60%
        45 = >=55%
        50 = >=50%
        55 = >=45%
        60 = >=40%
        65 = >=35%
        70 = >=30%
        75 = >=25%
        80 = >=20%
        85 = >=15%
        90 = >=10%
        95 = >=5%
        
        stat to index lookup
        0 = 19
        5 = 18
        10 = 17
        15 = 16
        20 = 15
        25 = 14
        30 = 13
        35 = 12
        40 = 11
        45 = 10
        50 = 9
        55 = 8
        60 = 7
        65 = 6
        70 = 5
        75 = 4
        80 = 3
        85 = 2
        90 = 1
        95 = 0
        '''
        self._coordinateLookup = {}
        # self._scentPercentLookup = {}
        # for i in range(0,20):
        #     x = str(i * 5 + 5) + '%'
        #     self._scentPercentLookup.update({x:i})
        self._scentPercentCoordinateLookup = [set() for i in range(0,20)] 

    def _get_stat_to_index(self, senseStat):
        #added if to prevent negative values
        if senseStat > 95:
            senseStat = 95
        return ((100 - senseStat)//5)- 1
    
    def _get_percent_to_index(self, percent):
        # removes %
        numConvertion = int(percent[:-1])
        #Added if to prevent negative values
        if numConvertion < 5:
            numConvertion = 5
        return numConvertion // 5 -1
    
    def _get_stealth_percent(self, level, stealthStat):
        return 100 - (level * 25) - ((stealthStat // 10) * 5)

    def _get_stealth_percent_string(self, level, stealthStat):
        return str(self._get_stealth_percent(level, stealthStat)) + '%'
    
    def _scent_search_top(self, position, level, stealthStat):
        #adds current position to array. Recursively searchs positions above itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level, stealthStat) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level, stealthStat), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1, stealthStat))
        return returnArray
    
    def _scent_search_right(self, position, level, stealthStat):
        #adds current position to array. Recursively searchs positions above, to it's right, and under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level, stealthStat) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level, stealthStat), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1, stealthStat))
        returnArray.extend(self._scent_search_right((position[0] + 1, position[1]), level + 1, stealthStat))
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1, stealthStat))
        return returnArray
    
    def _scent_search_bottom(self, position, level, stealthStat):
        #adds current position to array. Recursively searchs positions under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level, stealthStat) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level, stealthStat), position)]
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1, stealthStat))

        return returnArray

    def _scent_search_left(self, position, level, stealthStat):
        #adds current position to array. Recursively searchs positions above, to it's left, and under itself.
        if level > 3 or (position[0] < 0 or position[1] < 0) or self._get_stealth_percent(level, stealthStat) <= 0:
            return []

        returnArray = [(self._get_stealth_percent_string(level, stealthStat), position)]
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), level + 1, stealthStat))
        returnArray.extend(self._scent_search_left((position[0] - 1, position[1]), level + 1, stealthStat))
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), level + 1, stealthStat))

        return returnArray
    

    def _scent_search(self, position, stealthStat):
        returnArray = []
        returnArray.append((self._get_stealth_percent_string(0, stealthStat), position))

        #step 2) grab 4 adjacent neighbours as level 1 scent and then recursively find next 2 levels ending at level 3
        returnArray.extend(self._scent_search_top((position[0], position[1] + 1), 1, stealthStat))
        returnArray.extend(self._scent_search_right((position[0] + 1, position[1]), 1, stealthStat))
        returnArray.extend(self._scent_search_bottom((position[0], position[1] - 1), 1, stealthStat))
        returnArray.extend(self._scent_search_left((position[0] - 1, position[1]), 1, stealthStat))

        return returnArray

    def _update_scent_vars(self, scentPercent, scentCord):
        self._coordinateLookup.update({scentCord: scentPercent})
        self._scentPercentCoordinateLookup[scentPercent].update({scentCord})

    def get_scent_trail(self, senseStat):
        return self._scentPercentCoordinateLookup[self._get_stat_to_index(senseStat):]
    
    def add_scent_trail(self, scentList):
        #expects cords in the form (scent %, (x,y))
        for scent in scentList:
            scentPercent = self._get_percent_to_index(scent[0])
            scentCord = scent[1]
            
            if scentCord in self._coordinateLookup:
                currentScentLevel = self._coordinateLookup[scentCord]
                
                if currentScentLevel < scentPercent:
                    self._scentPercentCoordinateLookup[currentScentLevel].remove(scentCord)
                    self._update_scent_vars(scentPercent, scentCord)

            else:
                self._update_scent_vars(scentPercent, scentCord)
        

    def update_scent_trail(self, position, stealthStat):
        scentTrail = []
        
        # step 1) grab position lable as level 0 scent
        scentTrail.extend(self._scent_search(position, stealthStat))
        
        self.add_scent_trail(scentTrail)

    
    def scent_decay(self):
        #shift array left by 1 index
        self._scentPercentCoordinateLookup = self._scentPercentCoordinateLookup[1:]
        self._scentPercentCoordinateLookup.append(set())
        # shift coordinate look up values down by 1 to match
        self._coordinateLookup = {k:v - 1 for k,v in self._coordinateLookup.items() if v != 0}






def tester():
    tester1 = Scent()
    #print(tester1.get_scent_trail(50))

    # add scent Tester
    # print(tester1._scentPercentCoordinateLookup)
    # tester1.add_scent_trail([('55%',(1,3)), ('50%',(2,3)), ('5%',(4,3)), ('5%',(5,3)), ('5%',(5,4))])
    # print(tester1._scentPercentCoordinateLookup)
    # print(tester1._coordinateLookup)

    # print('------------------')
    # tester1.add_scent_trail([('10%',(5,4)), ('45%',(4,3))])
    # print(tester1._scentPercentCoordinateLookup)
    # print(tester1._coordinateLookup)

    # print('------------------')
    # tester1.add_scent_trail([('5%',(5,4)), ('30%',(4,3))])
    # print(tester1._scentPercentCoordinateLookup)
    # print(tester1._coordinateLookup)

    # print(tester1.get_scent_trail(60))

    # print('------------------')
    # print(tester1._scentPercentCoordinateLookup)
    # print(tester1._coordinateLookup)
    # tester1.scent_decay()
    # print(tester1._scentPercentCoordinateLookup)
    # print(tester1._coordinateLookup)

    tester1.update_scent_trail((50,50), 30)
    print(tester1._scentPercentCoordinateLookup)


if __name__ == '__main__':
    tester()