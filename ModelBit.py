import pygame
from ModelOrder import ModelOrder
from ModelLocation import ModelLocation
class InvalidOrderError(Exception):
    """
    Custom error that gets executed when the given order to the bit is not valid
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidLocationError(Exception):
    """
    Custom error that gets executed when the given location to the bit is not valid
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ModelBit:
    """
    Model part class that controls each individual bit
    """
    counter = 0 #Counts the number of bits existing
    kill_counter = 0 #Counts which was the last bit to die
    instances = [] #Saves the instances of ModelBit

    def __init__(self, name, locations, time=0.0, x=0, y=0, limit=100.0,
                 subsystem=False, critic=False, load=0.0, goto=False, fix=False,
                 mine=False, move=False):
        ModelBit.counter += 1

        self.name = name
        self.time = time    #Determines the remining lifetime of the bit
        # self.working = working  #Boolean that indicates if the bit is currently working or in standby
        self.subsystem = subsystem  #Boolean that indicates if the bit is working in a subsystem or not
        self.critic = critic    #Boolean that indicates if the bit is in critic state or not
        self.loc = 'BIOS'   #Location where the bit is currently positionated
        self.x = x
        self.y = y
        self.load = load
        self.limit = limit

        self.GoToCheck = goto
        self.FixCheck = fix
        self.MineCheck = mine
        self.MoveCheck = move
        self.GetDestination = ''
        self.StoreDestination = ''

        # List of hints of the orders a bit can get
        self.OrdList = ['MINE', 'FIX', 'GO TO', 'GET RESOURCE IN LOCATION', 'STORE RESOURCE IN LOCATION', 'MOVE RESOURCE FROM LOCATION TO LOCATION']
        # Complete orders that a bit can get:
        #    GO TO LOCATION, 3
        #    MINE, 1
        #    MOVE RESOURCE FROM LOCATION TO LOCATION, 5
        #    FIX LOCATION, 2
        #    GET RESOURCE FROM LOCATION, 4
        #    STORE RESOURCE IN LOCATION, 4

        # List of the valid locations
        # It will have to be the list obtained with the determined objects of ModelLocation
        # For now it will remain as it is, here is the code example for the LocationList made in main code:
        # Locations = [ModelLocation('PERI'), ModelLocation('VRM'), ModelLocation('RAM'),
        #            ModelLocation('ATX'), ModelLocation('CPU'), ModelLocation('DISK'),
        #            ModelLocation('CLK'), ModelLocation('BIOS'), ModelLocation('CHIPSET'),
        #            ModelLocation('GPU'), ModelLocation('VENT')]
        # LocList = []
        # for location in Locations:
        #    LocList.append(location.name)
        self.LocationList = locations
        self.LocationListNames = []
        for i in self.LocationList:
            self.LocationListNames.append(i.name)
        #['PERI', 'VRM', 'RAM', 'ATX', 'CPU', 'DISK', 'CLK', 'BIOS', 'CHIPSET', 'GPU', 'VENT']

        self.__class__.instances.append(self)

    #Function that checks if an order is real and calls for the correct method
    def receive_order(self, Ord):    #The variable Ord will be the order obtained from ModelOrder.CheckOrder
        if not self.subsystem:
            DecomposedOrd = Ord.split() #We get each word of the order into a new list
            numwords = len(DecomposedOrd)
            match numwords: #Determines what to deppending on the value of numwords
                case 1: #Case when the order is mine
                    if not self.MineCheck and not self.GoToCheck and not self.MoveCheck:
                        reference = self.OrdList[0]
                        if reference == DecomposedOrd:
                            self.MineCheck = True
                        else:
                            raise InvalidOrderError('INVALID ORDER')
                    elif self.MineCheck:
                        return ''
                case 2: #Case when the order is fix
                    if not self.GoToCheck and not self.MoveCheck:
                        reference = self.OrdList[1]
                        if reference == DecomposedOrd[0]:
                            destination = DecomposedOrd[1]
                            if destination not in self.LocationListNames:  # In case the given location is not found in the available list, raise the custom error
                                raise InvalidLocationError('GIVEN LOCATION DOES NOT EXIST')
                            else:
                                if self.loc != destination:
                                    raise InvalidOrderError('CANT FIX A LOCATION FROM DISTANCE')
                                elif self.loc == destination:
                                    self.MineCheck = False
                                    self.FixCheck = True
                                    self.subsystem = True
                        else:
                            raise InvalidOrderError('INVALID ORDER')
                case 3: #Case when the order is go to
                    reference = self.OrdList[2].split()
                    if reference[0] == DecomposedOrd[0] and reference[1] == DecomposedOrd[1]:
                        destination = DecomposedOrd[2]
                        if destination not in self.LocationListNames:  # In case the given location is not found in the available list, raise the custom error
                            raise InvalidLocationError('GIVEN LOCATION DOES NOT EXIST')
                        else:
                            if self.loc == destination:  # If the bit is already at the given location, do nothing
                                return ''
                            else:
                                self.loc = destination
                                self.MineCheck = False
                                self.MoveCheck = False
                                self.GoToCheck = True
                    else:
                        raise InvalidOrderError('INVALID ORDER')
                case 4: #Case when the order is get or store
                    if not self.GoToCheck and not self.MoveCheck:
                        GetReference = self.OrdList[3].split()
                        StoreReference = self.OrdList[4].split()
                        if GetReference[0] == DecomposedOrd[0] and GetReference[2] == DecomposedOrd[2]: #The order is a get
                            destination = DecomposedOrd[3]
                            if destination not in self.LocationListNames:
                                raise InvalidLocationError('GIVEN LOCATION DOES NOT EXIST')
                            else:
                                if destination != self.loc:
                                    return ''
                                else:
                                    self.MineCheck = False
                                    destination.give_power(self.name)

                        elif StoreReference[0] == DecomposedOrd[0] and StoreReference[2] == DecomposedOrd[2]: #The order is a store
                            destination = DecomposedOrd[3]
                            if destination not in self.LocationListNames:
                                raise InvalidLocationError('GIVEN LOCATION DOES NOT EXIST')
                            else:
                                if destination != self.loc:
                                    return ''
                                else:
                                    self.MineCheck = False
                                    destination.get_power(self.name)    #Method from ModelLocation that gets power from a bit
                        else:
                            raise InvalidOrderError('INVALID ORDER')
                case 5: #Case when the order is move
                    reference = self.OrdList[5].split()
                    if reference[0] == DecomposedOrd[0] and reference[2] == DecomposedOrd[2] and  reference[4] == DecomposedOrd[4]:
                        get_destination = DecomposedOrd[3]
                        store_destination = DecomposedOrd[5]
                        if get_destination not in self.LocationListNames or store_destination not in self.LocationListNames:
                            raise InvalidLocationError('GIVEN LOCATION DOES NOT EXISTS')
                        else:
                            self.GetDestination = get_destination
                            self.loc = get_destination
                            self.StoreDestination = store_destination
                            self.MoveCheck = True
                    else:
                        raise InvalidOrderError('INVALID ORDER')
                case _: #Raises custom error
                    raise InvalidOrderError('INVALID ORDER')
        else:
            raise InvalidOrderError('CANT RECEIVE AN ORDER WHILE IN A SUBSYSTEM')

    def go_to(self, destination): #Method that moves a bit to a designated location
        if self.GoToCheck:
            for location in self.LocationList:
                if location.name == destination:
                    new_x = location.x
                    new_y = location.y
            if self.x != new_x:
                if new_x < self.x:
                    self.x -= 10
                elif new_x > self.x:
                    self.x += 10
            if self.y != new_y:
                if new_y < self.y:
                    self.y -= 10
                elif new_y > self.y:
                    self.y += 10
            if self.x == new_x and self.y == new_y:
                self.GoToCheck = False
        elif not self.GoToCheck:
            print('Go to order has not been given yet')

    def fix(self, destination): #Method that gets a bit into the subsystem of a given location to fix it
        if self.FixCheck:
            destination.custom_alert(self.name) #We call to the custom_alert method from the given location
        elif not self.FixCheck:
            print('Fix order has not been given yet')

    def mine(self, destination):    #Method that gets a bit to start mining the location it is on at the moment
        if self.MineCheck:
            destination.get_mined(self.name)
        elif not self.MineCheck:
            print('Mine order has not been given yet')

    def move(self, GetDestination, StoreDestination): #Method that moves a bit from one place to another carrying power from 1 to 2
        if self.MoveCheck:
            self.GoToCheck = True
            if self.loc == GetDestination:  #Case when the bit is going to the location to get resources
                self.go_to(GetDestination)
                if not self.GoToCheck:
                    GetDestination.give_power(self.name)
                    self.loc = StoreDestination
            elif self.loc == StoreDestination:  #Case when the bit is going to the location to store resources
                self.go_to(StoreDestination)
                if not self.GoToCheck:
                    StoreDestination.get_power(self.name)
                    self.loc = GetDestination
        elif not self.MoveCheck:
            print('Move order has not been given yet')

def main():
    """Pruebas funcionamiento de órden go to"""
    # Uno = ModelBit([ModelLocation('PERI', 10, 10), ModelLocation('VRM', 20, 20), ModelLocation('RAM', 30, 30),
    #                 ModelLocation('ATX', 40, 40), ModelLocation('CPU', 50, 50), ModelLocation('DISK', 0, 0),
    #                 ModelLocation('CLK', -50, -50), ModelLocation('BIOS', -40, -40), ModelLocation('CHIPSET', -30, -30),
    #                 ModelLocation('GPU', -20, -20), ModelLocation('VENT', -10, -10)])
    # print(' Prueba bit 1 \n')
    # print(Uno.loc)
    # Uno.GoToCheck(Uno.loc)
    # Uno.ReceiveOrder('GO TO ATX')
    # print(Uno.loc)
    # while (Uno.go_to):
    #     Uno.GoToCheck(Uno.loc)
    #     print(Uno.x)
    #     print(Uno.y)
    #     print(Uno.go_to)
    #
    # Dos = ModelBit([ModelLocation('PERI', 10, 10), ModelLocation('VRM', 20, 20), ModelLocation('RAM', 30, 30),
    #                 ModelLocation('ATX', 40, 40), ModelLocation('CPU', 50, 50), ModelLocation('DISK', 0, 0),
    #                 ModelLocation('CLK', -50, -50), ModelLocation('BIOS', -40, -40), ModelLocation('CHIPSET', -30, -30),
    #                 ModelLocation('GPU', -20, -20), ModelLocation('VENT', -10, -10)])
    # print('\n Prueba bit 2 \n')
    # print(Dos.loc)
    # Dos.ReceiveOrder('GO TO BIOS')
    # print(Dos.loc)
    # Dos.GoToCheck(Dos.go_to)
    #
    # Tres = ModelBit([ModelLocation('PERI', 10, 10), ModelLocation('VRM', 20, 20), ModelLocation('RAM', 30, 30),
    #                 ModelLocation('ATX', 40, 40), ModelLocation('CPU', 50, 50), ModelLocation('DISK', 0, 0),
    #                 ModelLocation('CLK', -50, -50), ModelLocation('BIOS', -40, -40), ModelLocation('CHIPSET', -30, -30),
    #                 ModelLocation('GPU', -20, -20), ModelLocation('VENT', -10, -10)])
    # print('\n Prueba bit 3 \n')
    # print(Tres.loc)
    # Tres.ReceiveOrder('GO TO GPU')
    # print(Tres.loc)
    # while (Tres.go_to):
    #     Tres.GoToCheck(Tres.loc)
    #     print(Tres.x)
    #     print(Tres.y)
    #     print(Tres.go_to)
    #
    # Cuatr = ModelBit([ModelLocation('PERI', 10, 10), ModelLocation('VRM', 20, 20), ModelLocation('RAM', 30, 30),
    #                  ModelLocation('ATX', 40, 40), ModelLocation('CPU', 50, 50), ModelLocation('DISK', 0, 0),
    #                  ModelLocation('CLK', -50, -50), ModelLocation('BIOS', -40, -40),
    #                  ModelLocation('CHIPSET', -30, -30),
    #                  ModelLocation('GPU', -20, -20), ModelLocation('VENT', -10, -10)])
    # print('\n Prueba bit 4 \n')
    # print(Cuatr.loc)
    # Cuatr.ReceiveOrder('GO TO RAM')
    # print(Cuatr.loc)
    # i = 0
    # while (Cuatr.go_to):
    #     if i == 2:
    #         Cuatr.ReceiveOrder('GO TO CLK')
    #     Cuatr.GoToCheck(Cuatr.loc)
    #     print(Cuatr.x)
    #     print(Cuatr.y)
    #     print(Cuatr.go_to)
    #     i += 1



if __name__ == "__main__":
    main()