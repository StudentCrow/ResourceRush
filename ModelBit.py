import pygame
import ModelOrder
import ModelLocation

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
    def __init__(self, time = 0.0, working = False, subsystem = False, critic = False):
        self.time = time    #Determines the remining lifetime of the bit
        self.working = working  #Boolean that indicates if the bit is currently working or in standby
        self.subsystem = subsystem  #Boolean that indicates if the bit is working in a subsystem or not
        self.critic = critic    #Boolean that indicates if the bit is in critic state or not
        self.loc = 'BIOS'   #Location where the bit is currently positionated

        # List of hints of the orders a bit can get
        self.OrdList = ['MINE', 'FIX', 'GO TO', 'GET', 'STORE', 'MOVE']
        # Complete orders that a bit can get:
        #    GO TO LOCATION, 3
        #    MINE, 1
        #    MOVE RESOURCE FROM LOCATION TO LOCATION, 5
        #    FIX LOCATION, 2
        #    GET RESOURCE FROM LOCATION, 4
        #    STORE RESOURCE TO LOCATION, 4

        # List of the valid locations
        self.LocationList = ['PERI', 'VRM', 'RAM', 'ATX', 'CPU', 'DISK', 'CLK', 'BIOS', 'CHIPSET', 'GPU', 'VENT']

    #Function that checks if an order is real and calls for the correct method
    def ReceiveOrder(self, Ord):    #The variable Ord will be the order obtained from ModelOrder.CheckOrder
        DecomposedOrd = Ord.split() #We get each word of the order into a new list
        numwords = len(DecomposedOrd)
        match numwords: #Determines what to deppending on the value of numwords
            case 1: #Case when the order is mine
                for i in self.OrdList:
                    if self.OrdList.index(i) == 0:
                        if i ==  DecomposedOrd:
                            pass    #Start mine method
                        else:
                            raise InvalidOrderError('INVALID ORDER')
            case 2: #Case when the order is fix
                for i in self.OrdList:
                    if self.OrdList.index(i) == 1:
                        if i == DecomposedOrd[0]:
                            pass    #Start fix method
                        else:
                            raise InvalidOrderError('INVALID ORDER')
            case 3: #Case when the order is go to
                for i in self.OrdList:
                    if self.OrdList.index(i) == 2:
                        reference = i.split()
                        if reference[0] == DecomposedOrd[0] and reference[1] == DecomposedOrd[1]:
                            pass    #Start goto method
                        else:
                            raise InvalidOrderError('INVALID ORDER')
            case 4: #Case when the order is get or store
                for i in self.OrdList:
                    if self.OrdList.index(i) == 3:
                        GetReference = i
                        StoreReference = self.OrdList[self.OrdList.index(i)+1]
                        if GetReference == DecomposedOrd[0]:
                            pass    #Start get method
                        elif StoreReference == DecomposedOrd[0]:
                            pass    #Start store method
                        else:
                            raise InvalidOrderError('INVALID ORDER')
            case 5: #Case when the order is move
                for i in self.OrdList:
                    if self.OrdList.index(i) == 5:
                        reference = i
                        if reference == DecomposedOrd[0]:
                            pass    #Start move method
                        else:
                            raise InvalidOrderError('INVALID ORDER')
            case _: #Raises custom error
                raise InvalidOrderError('INVALID ORDER')

    def goto(self, destination): #Method that moves a bit to a designated location
        if destination not in self.LocationList:    #In case the given location is not found in the available list, raise the custom error
            raise InvalidLocationError('GIVEN LOCATION DOES NOT EXISTS')
        else:
            if self.loc == destination: #If the bit is already at the given location, do nothing
                return ''
            else:
                pass