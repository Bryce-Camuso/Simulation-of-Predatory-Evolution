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
        self._scentPercentCoordinateLookup = [set() for i in range(0,20)] #remove fill for testing

    def _get_stat_to_index(self, senseStat):
        #added if to prevent negative values
        if senseStat > 95:
            senseStat = 95
        return ((100 - senseStat)//5)- 1
    
    def _get_percent_to_index(self, percent):
        # remove %
        numConvertion = int(percent[:-1])
        #Added if to prevent negative values
        if numConvertion < 5:
            numConvertion = 5
        return numConvertion // 5 -1

    def _update_scent_trail(self, scentPercent, scentCord):
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
                    self._update_scent_trail(scentPercent, scentCord)

            else:
                self._update_scent_trail(scentPercent, scentCord)
        
            
    
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



if __name__ == '__main__':
    tester()