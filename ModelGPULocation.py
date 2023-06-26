from random import *

class ModelGPU:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.graphics = 0.0
        self.consumption = 170.0
        self.alert_percentage = 0
        self.alert_counter = {'GRAPHICS': 0, 'GRAPHICS NW': 0, 'POWER': 0, 'TEMPERATURE': 0}

    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.graphics = 0.0

    def manageAlerts(self):
        if self.functional:
            ###
            # Random increase of graphics usage between 0% and 10%
            self.generateResource()
            ###
            # Graphics errors
            if self.graphics >= 0.8 and self.alert_counter['GRAPHICS'] == 0:  # Activates the too much graphic usage alert
                self.alert_counter['GRAPHICS'] += 1
            elif self.graphics < 0.8 and self.alert_counter['GRAPHICS'] != 0:  # Deactivates the too much graphic usage alert
                self.alert_counter['GRAPHICS'] -= 1

            if self.graphics > 0.65 and self.alert_counter['GRAPHICS NW'] == 0:  # Activates with a 15% chance the GRAPHICS NW error if graphic usage abive 65%
                error = round(random(), 2)
                if error > 0.85:  # 15% chance for the error to trigger
                    self.alert_counter['GRAPHICS NW'] += 1
                    self.alert_percentage += 100
                    self.graphics = 0.0
            ###
            # Temperature error
            if self.temperature >= 93.0 and self.alert_counter['TEMPERATURE'] == 0:
                self.alert_counter['TEMPERATURE'] += 1
            elif self.temperature < 93.0 and self.alert_counter['TEMPERATURE'] != 0:
                self.alert_counter['TEMPERATURE'] -= 1
            ###
            # Power error
            if self.power <= 425.0 and self.alert_counter['POWER'] == 0:
                self.alert_counter['POWER'] += 1
            elif self.power > 425.0 and self.alert_counter['POWER'] != 0:
                self.alert_counter['POWER'] -= 1
            ###
            
    def customAlert(self, bit):
        if self.functional:
            if self.alert_counter['GRAPHICS NW'] != 0 and bit.subsystem:  # If there is an error it starts fixing it
                self.alert_percentage -= randrange(0, 4)  # Decreases the percentage of error left to fix in a random from 1 to 3
                if self.alert_percentage <= 0:  # If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                    self.alert_percentage = 0
                    self.alert_counter['GRAPHICS NW'] -= 1
                    bit.subsystem = False
                    bit.FixCheck = False
            elif self.alert_counter['GRAPHICS NW'] == 0 and bit.subsystem:  # In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                bit.subsystem = False
                bit.FixCheck = False
        else:
            bit.subsystem = False
            bit.FixCheck = False

    def tempIncrease(self):
        if self.functional:
            if self.graphics <= 0.89:
                if self.temperature < 75.0: self.temperature += 1.0
            else:
                self.temperature = self.consumption * (self.graphics - 0.89) + 75.0

    def powerManagament(self):
        if self.power >= self.consumption:
            if not self.functional: self.functional = True
            variable_consumption = self.graphics - 0.9
            if variable_consumption < 0: variable_consumption = 0
            self.power -= self.consumption * variable_consumption + self.consumption
            if self.power < 0: self.power = 0
        else:
            self.resetLocation()

    def generateResource(self):
        if self.alert_counter['GRAPHICS NW'] == 0:  # Graphics only increase if working
            if self.graphics < 1: self.graphics += round(uniform(0.0, 0.1), 2)
            elif self.graphics >= 1: self.graphics += round(uniform(0.0, 0.03), 2)  # Graphic usage rises slower because it will generate too much heat, aka, temperature error
            
    def getMined(self):
        if self.functional:
            if self.alert_counter['GRAPHICS NW'] == 0: self.graphics -= round(uniform(0.005, 0.03), 2)

    def get_power(self, bit):    #Method for when a bit gives power to a location
        charge = bit.load
        self.power += charge
        bit.load = 0

    def give_power(self, bit):  #Method for when a bit gets power from a location
        charge = bit.limit - bit.load
        self.power -= charge
        bit.load += charge