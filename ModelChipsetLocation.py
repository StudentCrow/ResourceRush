from random import *

class ModelCHIPSET:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.chipset_power = 0.0
        self.consumption = 8.55
        self.alert_counter = {'CHIPSET': 0, 'POWER': 0, 'TEMPERATURE': 0}

    def resetLocation(self):
        self.functional = False; self.temperature = 0.0; self.chipset_power = 0.0
        for name in self.alert_counter:
            if name != 'POWER': self.alert_counter[name] = 0
    
    def manageAlerts(self):
        ###
        # Chipset output error
        if self.chipset_power <= 30.0 and self.alert_counter['CHIPSET'] == 0:
            self.alert_counter['CHIPSET'] += 1
        elif self.chipset_power > 30.0 and self.alert_counter['CHIPSET'] != 0:
            self.alert_counter['CHIPSET'] -= 1
        ###
        # Temperature error
        if self.temperature >= 55.0 and self.alert_counter['TEMPERATURE'] == 0:
            self.alert_counter['TEMPERATURE'] += 1
        elif self.temperature < 55.0 and self.alert_counter['TEMPERATURE'] != 0:
            self.alert_counter['TEMPERATURE'] -= 1
        ###
        # Power error
        if self.power <= 21.38 and self.alert_counter['POWER'] == 0:
            self.alert_counter['POWER'] += 1
        elif self.power > 21.38 and self.alert_counter['POWER'] != 0:
            self.alert_counter['POWER'] -= 1
        ###

    def customAlert(self, bit):
        if bit.subsystem:
            bit.subsystem = False
            bit.FixCheck = False

    def tempIncrease(self):
        if self.chipset_power <= 40.0: self.temperature += 1.0
        else: self.temperature = self.consumption * ((self.chipset_power / 100.0) + 1.59) + 30.0

    def powerManagement(self):
        if self.power >= self.consumption and self.temperature <= 65.0:
            if not self.functional: self.functional = True
            variable_consumption = (self.chipset_power / 100) - 1.5
            if variable_consumption < 0: variable_consumption = 0
            self.power -= self.consumption * variable_consumption + self.consumption
            if self.power < 0: self.power = 0
        else:
            self.resetLocation()

    def generateResource(self):
        self.chipset_power += round(uniform(0.0, 3.0), 2)

    def getMined(self):
        if self.functional: self.generateResource()

    def get_power(self, bit):    #Method for when a bit gives power to a location
        charge = bit.load
        self.power += charge
        bit.load = 0

    def give_power(self, bit):  #Method for when a bit gets power from a location
        charge = bit.limit - bit.load
        self.power -= charge
        bit.load += charge

    def updateLocInfo(self):
        alerts = 0
        for a in self.alert_counter:
            alerts += self.alert_counter[a]
        info = [self.power, self.temperature, self.chipset_power, alerts]
        return info

    def work(self):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        self.powerManagement()