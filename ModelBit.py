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
    def __init__(self, locations, time = 0.0, working = False, subsystem = False, critic = False, x = 0, y = 0, go_to = False):
        #self.image = pygame.image.load(img_path)    #Load sprite

        self.time = time    #Determines the remining lifetime of the bit
        self.working = working  #Boolean that indicates if the bit is currently working or in standby
        self.subsystem = subsystem  #Boolean that indicates if the bit is working in a subsystem or not
        self.critic = critic    #Boolean that indicates if the bit is in critic state or not
        self.loc = 'BIOS'   #Location where the bit is currently positionated
        self.x = x
        self.y = y

        self.go_to = go_to

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
                            destination = DecomposedOrd[2]
                            if destination not in self.LocationListNames:  # In case the given location is not found in the available list, raise the custom error
                                raise InvalidLocationError('GIVEN LOCATION DOES NOT EXISTS')
                            else:
                                if self.loc == destination:  # If the bit is already at the given location, do nothing
                                    return ''
                                else:
                                    for location in self.LocationListNames:  # Determine the new bit location and let the goto method work by changing its asigned bool
                                        if location == destination:
                                            self.loc = destination
                                            self.go_to = True
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
        if self.go_to:
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
                self.go_to = False

    def draw(self, surface): #Method to blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))