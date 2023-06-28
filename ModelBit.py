class ModelBit:
    """
    Model part class that controls each individual bit
    """

    def __init__(self, name, locations, x=0, y=0, load=0.0):
        self.name = name
        #self.time = 0.0    #Determines the remining lifetime of the bit
        self.loc = 'BIOS'   #Location where the bit is currently positionated
        self.x = x
        self.y = y
        self.center = [x, y]
        self.load = load
        self.limit = 100.0
        self.idle = True
        self.GoToCheck = False
        self.FixCheck = False
        self.MineCheck = False
        self.MoveCheck = False
        self.GetDestination = ''
        self.StoreDestination = ''
        # List of hints of the orders a bit can get
        self.OrdList = ['MINE', 'FIX', 'GO TO', 'GET P FROM LOCATION', 'STORE P IN LOCATION', 'MOVE P FROM LOCATION TO LOCATION']
        # Complete orders that a bit can get:
        #    GO TO LOCATION, 3
        #    MINE, 1
        #    MOVE RESOURCE FROM LOCATION TO LOCATION, 6
        #    FIX LOCATION, 2
        #    GET RESOURCE FROM LOCATION, 4
        #    STORE RESOURCE IN LOCATION, 4
        self.LocationList = locations
        self.LocationListNames = []
        for i in self.LocationList:
            self.LocationListNames.append(i.name)

    #Function that checks if an order is real and calls for the correct method
    def receive_order(self, Ord):    #The variable Ord will be the order obtained from ModelOrder.CheckOrder
        DecomposedOrd = Ord.split() #We get each word of the order into a new list
        numwords = len(DecomposedOrd)
        match numwords: #Determines what to deppending on the value of numwords
            case 1: #Case when the order is mine
                if not self.MineCheck and not self.GoToCheck and not self.MoveCheck:
                    reference = self.OrdList[0]
                    if reference == DecomposedOrd[0]:
                        self.FixCheck = False
                        self.MineCheck = True
                    else:
                        return ''
                elif self.MineCheck:
                    return ''
            case 2: #Case when the order is fix
                if not self.GoToCheck and not self.MoveCheck:
                    reference = self.OrdList[1]
                    if reference == DecomposedOrd[0]:
                        destination = DecomposedOrd[1]
                        if destination not in self.LocationListNames:  # In case the given location is not found in the available list, raise the custom error
                            return ''
                        else:
                            if self.loc != destination:
                                return ''
                            elif self.loc == destination:
                                self.MineCheck = False
                                self.FixCheck = True
                    else:
                        return ''
            case 3: #Case when the order is go to
                reference = self.OrdList[2].split()
                if reference[0] == DecomposedOrd[0] and reference[1] == DecomposedOrd[1]:
                    destination = DecomposedOrd[2]
                    if destination not in self.LocationListNames:  # In case the given location is not found in the available list, raise the custom error
                        return ''
                    else:
                        if self.loc == destination:  # If the bit is already at the given location, do nothing
                            return ''
                        else:
                            self.loc = destination
                            self.FixCheck = False
                            self.MineCheck = False
                            self.MoveCheck = False
                            self.GoToCheck = True
                else:
                    return ''
            case 4: #Case when the order is get or store
                if not self.GoToCheck and not self.MoveCheck:
                    GetReference = self.OrdList[3].split()
                    StoreReference = self.OrdList[4].split()
                    if GetReference[0] == DecomposedOrd[0] and GetReference[2] == DecomposedOrd[2]: #The order is a get
                        destination = DecomposedOrd[3]
                        if destination not in self.LocationListNames:
                            return ''
                        else:
                            if destination != self.loc:
                                return ''
                            else:
                                self.FixCheck = False
                                self.MineCheck = False
                                for loc in self.LocationList:
                                    if loc.name == destination: loc.givePower(self.name)

                    elif StoreReference[0] == DecomposedOrd[0] and StoreReference[2] == DecomposedOrd[2]: #The order is a store
                        destination = DecomposedOrd[3]
                        if destination not in self.LocationListNames:
                            return ''
                        else:
                            if destination != self.loc:
                                return ''
                            else:
                                self.FixCheck = False
                                self.MineCheck = False
                                for loc in self.LocationList:
                                    if loc.name == destination: loc.getPower(self.name)
                    else:
                        return ''
            case 6: #Case when the order is move
                reference = self.OrdList[5].split()
                if reference[0] == DecomposedOrd[0] and reference[1] == DecomposedOrd[1] and reference[2] == DecomposedOrd[2] and  reference[4] == DecomposedOrd[4]:
                    get_destination = DecomposedOrd[3]
                    store_destination = DecomposedOrd[5]
                    if get_destination not in self.LocationListNames or store_destination not in self.LocationListNames:
                        return ''
                    else:
                        self.GetDestination = get_destination
                        self.loc = get_destination
                        self.StoreDestination = store_destination
                        self.FixCheck = False
                        self.MineCheck = False
                        self.MoveCheck = True
                else:
                    return ''
            case _:
                return ''

    def go_to(self, destination): #Method that moves a bit to a designated location
        if self.idle: self.idle = False
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
                if new_x-new_x*0.05 <= self.x <= new_x+new_x*0.05 and new_y-new_y*0.05 <= self.y <= new_y+new_y*0.05:
                    self.center = [self.x, self.y]
                    self.GoToCheck = False
                    self.idle = True

    def fix(self, destination): #Method that gets a bit into the subsystem of a given location to fix it
        for loc in self.LocationList:
            if loc.name == destination:
                loc.customAlert(self.name) #We call to the custom_alert method from the given location

    def mine(self, destination):    #Method that gets a bit to start mining the location it is on at the moment
        for location in self.LocationList:
            if location.name == destination:
                location.getMined()

    def move(self, GetDestination, StoreDestination): #Method that moves a bit from one place to another carrying power from 1 to 2
        if not self.GoToCheck: self.GoToCheck = True
        if self.loc == GetDestination:  #Case when the bit is going to the location to get resources
            self.go_to(GetDestination)
            if not self.GoToCheck:
                for location in self.LocationList:
                    if location.name == GetDestination:
                        location.givePower(self.name)
                self.loc = StoreDestination
        elif self.loc == StoreDestination:  #Case when the bit is going to the location to store resources
            self.go_to(StoreDestination)
            if not self.GoToCheck:
                for location in self.LocationList:
                    if location.name == StoreDestination:
                        location.getPower(self.name)
                self.loc = GetDestination