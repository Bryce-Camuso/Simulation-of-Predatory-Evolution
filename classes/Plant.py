from Scent import Scent


class Plant:

    def __init__(self, position):
        self._position = position
        self._scent = Scent()

    def get_position(self):
        return self._position
    
    def get_scent(self):
        return self._scent
    
    def set_position(self, newPosition):
        if not isinstance(newPosition, tuple):
            raise TypeError('Position must be a tuple')
        if newPosition[0] < 0 or newPosition[1] < 0:
            raise ValueError('new position can not be negative.')
        self._position = newPosition

    def update_scent_trail(self):
        self._scent.update_scent_trail(self.get_position(), 0)



def tester():
    plant1 = Plant((4,4))
    scentTest = Scent()

    #getters
    print('Getters')

    if plant1.get_position() == (4,4):
        print('position: pass')
    else:
        print('position: fail')

    if isinstance(plant1.get_scent(), Scent):
        print('scent: pass')
    else:
        print('scent: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    print('\nSetters')

    plant1.set_position((10,10))

    if plant1.get_position() == (10,10):
        print('position: pass')
    else:
        print('position: fail')


    print('---------------------------------------------------------------------------------------------------------------------')

    #setters errors
    print('\nSetters Errors')

    try:
        plant1.set_position(1)
        print('Error: None')
    except TypeError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        plant1.set_position((-1, 1))
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')

    try:
        plant1.set_position((1, -1))
        print('Error: None')
    except ValueError:
        print('Error: correct')
    except Exception as e:
        print('Error: incorrect ')


    print('---------------------------------------------------------------------------------------------------------------------')

    #setters valid edge cases
    print('\nSetters valid edge cases')
    
    plant1.set_position((0,0))
    if plant1.get_position() == (0,0):
        print('position: pass')
    else:
        print('position: fail')

    print('---------------------------------------------------------------------------------------------------------------------')

    #methods
    print('\nUpdate Scent Trail')

    plant1.set_position((30,30))

    plant1.update_scent_trail()
    scentTest.update_scent_trail((30,30), 0)

    testFlag = True
    testScent = plant1.get_scent().get_scent_trail(100)
    exampleObj = scentTest.get_scent_trail(100)
    for i in range(len(exampleObj)):
        if exampleObj[i] - testScent[i] != set():
            testFlag = False

    if testFlag:
        print('Update check: pass')
    else:
        print('Update check: false')






if __name__ == '__main__':
    tester()