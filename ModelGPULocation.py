from random import *

class ModelGPU:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.graphics = 0.0
        self.consumption = 70.0
        self.alert_percentage = 0
        self.alert = False
        self.alert_counter = {'GRAPHICS': 0, 'GRAPHICS NW': 0, 'POWER': 0, 'TEMPERATURE': 0}

    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.graphics = 0.0; self.alert_percentage = 0
        for name in self.alert_counter:
            if name != 'GRAPHICS NW' or 'POWER': self.alert_counter[name] = 0

    def manageAlerts(self):
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
            error = random()
            if error > 0.95:  # 5% chance for the error to trigger
                self.alert = True
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
            
    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                if self.functional:
                    if self.alert_counter['GRAPHICS NW'] != 0 and bit.FixCheck:  # If there is an error it starts fixing it
                        self.alert_percentage -= randrange(1, 10)  # Decreases the percentage of error left to fix in a random from 1 to 3
                        if self.alert_percentage <= 0:  # If there is no more error to be fixed, it gets deleted and the bit exits the subsystem
                            self.alert_percentage = 0
                            self.alert_counter['GRAPHICS NW'] -= 1
                            self.alert = False
                            bit.FixCheck = False
                    elif self.alert_counter['GRAPHICS NW'] == 0 and bit.FixCheck:  # In case there were more than one bit working to fix the error and it is already fixed, they get dismissed from the task
                        bit.FixCheck = False
                else:
                    bit.FixCheck = False

    def tempIncrease(self):
        if self.graphics <= 0.89:
            if self.temperature < 75.0: self.temperature += 1.0
        else:
            self.temperature = self.consumption * (self.graphics - 0.89) + 75.0

    def powerManagement(self):
        variable_consumption = self.graphics - 0.9
        if variable_consumption < 0: variable_consumption = 0
        self.power -= self.consumption * variable_consumption + self.consumption
        if self.power < 0: self.power = 0

    def generateResource(self):
        if self.alert_counter['GRAPHICS NW'] == 0:  # Graphics only increase if working
            if self.graphics < 1: self.graphics += round(uniform(0.0, 0.1), 2)
            elif self.graphics >= 1: self.graphics += round(uniform(0.0, 0.03), 2)  # Graphic usage rises slower because it will generate too much heat, aka, temperature error
            
    def getMined(self):
        if self.functional:
            if self.alert_counter['GRAPHICS NW'] == 0 and self.graphics != 0:
                self.graphics -= round(uniform(0.005, 0.03), 2)
                if self.graphics < 0: self.graphics = 0.0

    def getPower(self, name):  # Method for when a bit gives power to a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.load
                self.power += charge
                bit.load = 0

    def givePower(self, name):  # Method for when a bit gets power from a location
        for bit in self.bit_list:
            if bit.name == name:
                charge = bit.limit - bit.load
                self.power -= charge
                bit.load += charge

    def updateLocInfo(self):
        alerts = 0
        for a in self.alert_counter:
            alerts += self.alert_counter[a]
        info = {'P':self.power, 'T':self.temperature, 'G':self.graphics, 'A':alerts, 'AP':self.alert_percentage}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.power >= self.consumption:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()