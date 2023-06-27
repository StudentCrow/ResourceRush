from random import *

class ModelATX:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = True
        self.power = 0.0
        self.alert = False
        self.alert_counter = {'STORED POWER': 0}

    def resetLocation(self):
        self.power = 0.0

    def manageAlerts(self):
        ###
        #Stored power error
        if self.power >= 3500.0 and self.alert_counter['STORED POWER'] == 0:
            self.alert_counter['STORED POWER'] += 1
        elif self.power < 3500.0 and self.alert_counter['STORED POWER'] != 0:
            self.alert_counter['STORED POWER'] -= 1
        ###

    def customAlert(self, bit):
        if bit.subsystem:
            bit.subsystem = False
            bit.FixCheck = False

    def powerManagement(self):
        if self.power > 4500: self.resetLocation()

    def generateResource(self):
        self.power += round(uniform(10.0, 15.0), 2)

    def getMined(self):
        self.generateResource()

    def getPower(self, bit):    #Method for when a bit gives power to a location
        return ''

    def givePower(self, bit):  #Method for when a bit gets power from a location
        charge = bit.limit - bit.load
        self.power -= charge
        bit.load += charge

    def updateLocInfo(self):
        alerts = 0
        for a in self.alert_counter:
            alerts += self.alert_counter[a]
        info = {'P':self.power, 'A':alerts}
        return info

    def work(self):
        self.manageAlerts()
        self.powerManagement()