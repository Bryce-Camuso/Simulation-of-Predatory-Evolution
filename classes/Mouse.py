from Prey import Prey

class Mouse(Prey):
    # this class is just an interface for the prey class

    def __init__(self, speed, stealth, stamina, sense, position):
        super().__init__(speed, stealth, stamina, sense, position)




def tester():
    pass


if __name__ == '__main__':
        tester()