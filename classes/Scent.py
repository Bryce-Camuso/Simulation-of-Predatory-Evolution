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
        return numConvertion // 5 - 1
    
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

    
    # Methods
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
    tester2 = Scent()
    tester3 = Scent()

    print('\nGet scent trail')
    if len(tester1.get_scent_trail(0)) == 1:
        print('Scence 0: pass')
    else:
        print('Scence 0: fail')

    if len(tester1.get_scent_trail(5)) == 2:
        print('Scence 5: pass')
    else:
        print('Scence 5: fail')
    
    if len(tester1.get_scent_trail(10)) == 3:
        print('Scence 10: pass')
    else:
        print('Scence 10: fail')
    
    if len(tester1.get_scent_trail(15)) == 4:
        print('Scence 15: pass')
    else:
        print('Scence 15: fail')
    
    if len(tester1.get_scent_trail(20)) == 5:
        print('Scence 20: pass')
    else:
        print('Scence 20: fail')

    if len(tester1.get_scent_trail(25)) == 6:
        print('Scence 25: pass')
    else:
        print('Scence 25: fail')

    if len(tester1.get_scent_trail(30)) == 7:
        print('Scence 30: pass')
    else:
        print('Scence 30: fail')

    if len(tester1.get_scent_trail(35)) == 8:
        print('Scence 35: pass')
    else:
        print('Scence 35: fail')
    
    if len(tester1.get_scent_trail(40)) == 9:
        print('Scence 40: pass')
    else:
        print('Scence 40: fail')

    if len(tester1.get_scent_trail(45)) == 10:
        print('Scence 45: pass')
    else:
        print('Scence 45: fail')

    if len(tester1.get_scent_trail(50)) == 11:
        print('Scence 50: pass')
    else:
        print('Scence 50: fail')

    if len(tester1.get_scent_trail(55)) == 12:
        print('Scence 55: pass')
    else:
        print('Scence 55: fail')
    
    if len(tester1.get_scent_trail(60)) == 13:
        print('Scence 60: pass')
    else:
        print('Scence 60: fail')
    
    if len(tester1.get_scent_trail(65)) == 14:
        print('Scence 65: pass')
    else:
        print('Scence 65: fail')

    if len(tester1.get_scent_trail(70)) == 15:
        print('Scence 70: pass')
    else:
        print('Scence 70: fail')

    if len(tester1.get_scent_trail(75)) == 16:
        print('Scence 75: pass')
    else:
        print('Scence 75: fail')

    if len(tester1.get_scent_trail(80)) == 17:
        print('Scence 80: pass')
    else:
        print('Scence 80: fail')

    if len(tester1.get_scent_trail(85)) == 18:
        print('Scence 85: pass')
    else:
        print('Scence 85: fail')

    if len(tester1.get_scent_trail(90)) == 19:
        print('Scence 90: pass')
    else:
        print('Scence 90: fail')

    if len(tester1.get_scent_trail(95)) == 20:
        print('Scence 95: pass')
    else:
        print('Scence 95: fail')

    if len(tester1.get_scent_trail(100)) == 20:
        print('Scence 100: pass')
    else:
        print('Scence 100: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nAdd scent trail')
    tester1.add_scent_trail([('5%', (0,0))])
    exampleArray = [set() for i in range(0,20)]
    exampleArray[0].update({(0,0)})
    testFlag = True
    testScent = tester1.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if testScent[i] - exampleArray[i] != set():
            testFlag = False

    if testFlag:
        print('Add scent 5%: pass')
    else:
        print('Add scent 5%: false')

    tester1.add_scent_trail([('10%', (0,1)), ('15%', (0,2)), ('20%', (0,3)), ('25%', (0,4)), ('30%', (0,5)), ('35%', (0,6)), ('40%', (0,7)), ('45%', (0,8)), ('50%', (0,9)), ('55%', (0,10)), ('60%', (0,11)), ('65%', (0,12)), ('70%', (0,13)), ('75%', (0,14)), ('80%', (0,15)), ('85%', (0,16)), ('90%', (0,17)), ('95%', (0,18)), ('100%', (0,19))])
    exampleArray = [{(0,i)} for i in range(0,20)]
    testFlag = True
    testScent = tester1.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i]  != set():
            testFlag = False

    if testFlag:
        print('Add scent full: pass')
    else:
        print('Add scent full: fail')
    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nUpdate scent trail')
    tester2.update_scent_trail((30,30),0)

    exampleArray = [set() for i in range(0,20)]
    exampleArray[19].update({(30,30)})
    exampleArray[14].update({(31,30), (30,31), (29,30), (30,29)})
    exampleArray[9].update({(31, 29), (28, 30), (30, 28), (32, 30), (29, 31), (29, 29), (30, 32), (31, 31)})
    exampleArray[4].update({(32, 31), (30, 27), (30, 33), (27, 30), (28, 29), (31, 32), (29, 32), (29, 28), (32, 29), (28, 31), (31, 28), (33, 30)})
    testFlag = True
    testScent = tester2.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i]  != set():
            testFlag = False

    if testFlag:
        print('Update scent trail: pass')
    else:
        print('Update scent trail: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nScent decay')

    tester3.update_scent_trail((30,30),100)
    exampleArray = tester3.get_scent_trail(100)

    tester3.scent_decay()
    exampleArray.pop(0)
    exampleArray.append(set())
    testFlag = True
    testScent = tester3.get_scent_trail(100)

    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Scent decay 1: pass')
    else:
        print('Scent decay 1: false')
        
    tester3.scent_decay()
    exampleArray.pop(0)
    exampleArray.append(set())
    testFlag = True
    testScent = tester3.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i]  != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 2: pass')
    else:
        print('Scent decay 2: false')

    tester3.scent_decay()
    exampleArray.pop(0)
    exampleArray.append(set())
    testFlag = True
    testScent = tester3.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i] != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 3: pass')
    else:
        print('Scent decay 3: false')

    tester3.scent_decay()
    exampleArray.pop(0)
    exampleArray.append(set())
    testFlag = True
    testScent = tester3.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i] != set():
            testFlag = False
    
    if testFlag:
        print('Scent decay 4: pass')
    else:
        print('Scent decay 4: false')

    tester3.scent_decay()
    exampleArray.pop(0)
    exampleArray.append(set())
    testFlag = True
    testScent = tester3.get_scent_trail(100)
    for i in range(len(exampleArray)):
        if exampleArray[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Scent decay 5: pass')
    else:
        print('Scent decay 5: false')
    



if __name__ == '__main__':
    tester()