from random import *

class ModelCHIPSET:
    def __init__(self, name, x, y):
        self.bit_list = []
        self.name = name
        self.x = x
        self.y = y
        self.functional = False
        self.power = 0.0
        self.temperature = 0.0
        self.chipset_power = 0.0
        self.consumption = 8.55
        self.alert = False
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

    def customAlert(self, model_bit):
        for bit in self.bit_list:
            if bit.name == model_bit:
                if bit.FixCheck: bit.FixCheck = False

    def tempIncrease(self):
        if self.chipset_power <= 40.0: self.temperature += 1.0
        else: self.temperature = self.consumption * ((self.chipset_power / 100.0) + 1.59) + 30.0

    def powerManagement(self):
        variable_consumption = (self.chipset_power / 100) - 1.5
        if variable_consumption < 0: variable_consumption = 0
        self.power -= self.consumption * variable_consumption + self.consumption
        if self.power < 0: self.power = 0

    def generateResource(self):
        self.chipset_power += round(uniform(0.0, 3.0), 2)

    def getMined(self):
        if self.functional: self.generateResource()

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
        info = {'P':self.power, 'T':self.temperature, 'CP':self.chipset_power, 'A':alerts}
        return info

    def work(self, loc_event):
        if self.functional:
            self.manageAlerts()
            self.tempIncrease()
        if self.power >= self.consumption and self.temperature <= 65.0:
            if not self.functional: self.functional = True
            if loc_event == 10: self.powerManagement()
        else:
            if self.functional: self.resetLocation()