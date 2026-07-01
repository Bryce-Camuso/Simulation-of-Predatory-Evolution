from Prey import Prey


class Rabbit(Prey):
    #burrows are considered to be under all bush tiles


    def __init__(self, speed, stealth, stamina, sense, position):
        super().__init__(speed, stealth, stamina, sense, position)

    # Helper Functions
    def _pursuit_tile_weight(self, tileNum):
        if tileNum == 1:
            return 20
        if tileNum == 2:
            return -100
        if tileNum == 3:
            return 100

    # methods 
    def check_escape(self, map):
        position = self.get_position()
        tile = map.get_map_point(position)
        if tile[1] == 3:
            self.set_escaped(True)





def tester():
    pass


if __name__ == '__main__':
        tester()