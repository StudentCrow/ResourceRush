import pygame
import ModelOrder

class InvalidOrderError(Exception):
    """
    Custom error that gets executed when the given order to the bit is not valid
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class ModelBit:
    """
    Model part class that controls each individual bit
    """
    #List of hints of the orders a bit can get
    OrdList = ['GO TO', 'MINE', 'MOVE', 'FIX', 'GET', 'STORE']
    #Complete orders that a bit can get:
    #    GO TO LOCATION, 3
    #    MINE, 1
    #    MOVE RESOURCE FROM LOCATION TO LOCATION, 5
    #    FIX LOCATION, 2
    #    GET RESOURCE FROM LOCATION, 4
    #    STORE RESOURCE TO LOCATION, 4
    def __init__(self, time = 0.0, working = False, subsystem = False, critic = False):
        self.time = time    #Determines the remining lifetime of the bit
        self.working = working  #Boolean that indicates if the bit is currently working or in standby
        self.subsystem = subsystem  #Boolean that indicates if the bit is working in a subsystem or not
        self.critic = critic    #Boolean that indicates if the bit is in critic state or not
        self.loc = 'BIOS'   #Location where the bit is currently positionated

    #Function that checks if an order is real and calls for the correct method
    def ReceiveOrder(self, Ord):    #The variable Ord will be the order obtained from ModelOrder.CheckOrder
        DecomposedOrd = Ord.split #We get each word of the order into a new list
        numwords = len(DecomposedOrd)
        match numwords: #Determines what to deppending on the value of numwords
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _: #Raises custom error
                raise InvalidOrderError('Invalid order')